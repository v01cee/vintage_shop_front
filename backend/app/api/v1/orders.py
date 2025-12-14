"""
API endpoints для заказов с БД и JWT аутентификацией
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
import random
import string
from app.database import get_db
from app.models import Order, OrderItem, Product, CartItem
from app.schemas.order import Order as OrderSchema, OrderCreate, OrderUpdate, OrderItem as OrderItemSchema
from app.auth import get_current_user, get_current_user_optional
from app.models import User
from app.exceptions import NotFoundError, ValidationError, DatabaseError, ForbiddenError
from app.validators import validate_price, validate_quantity, validate_order_status

router = APIRouter()


def generate_order_number() -> str:
    """Генерация уникального номера заказа"""
    return ''.join(random.choices(string.digits, k=9))


@router.get("/orders", response_model=List[OrderSchema])
async def get_orders(
    status_filter: Optional[str] = Query(None, alias="status", description="Фильтр по статусу"),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Получить список заказов
    
    Если пользователь авторизован, возвращает только его заказы.
    Если не авторизован, возвращает все заказы (для админов, требует дополнительную проверку).
    
    - **status**: Фильтр по статусу (new, paid, in_progress, sent, cancelled, return)
    """
    query = db.query(Order)
    
    # Если пользователь авторизован, показываем только его заказы
    if current_user:
        query = query.filter(Order.user_id == current_user.id)
    
    if status_filter:
        validate_order_status(status_filter)
        query = query.filter(Order.status == status_filter)
    
    orders = query.order_by(Order.created_at.desc()).all()
    return orders


@router.get("/orders/{order_id}", response_model=OrderSchema)
async def get_order(
    order_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Получить заказ по ID
    
    Пользователь может получить только свои заказы.
    
    - **order_id**: ID заказа
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Проверяем права доступа
    if current_user and order.user_id != current_user.id:
        raise ForbiddenError("Можно просматривать только свои заказы")
    
    return order


@router.get("/orders/search/{order_number}", response_model=OrderSchema)
async def search_order_by_number(
    order_number: str,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Поиск заказа по номеру
    
    Пользователь может найти только свои заказы.
    
    - **order_number**: Номер заказа
    """
    order = db.query(Order).filter(Order.order_number == order_number).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Проверяем права доступа
    if current_user and order.user_id != current_user.id:
        raise ForbiddenError("Можно просматривать только свои заказы")
    
    return order


@router.post("/orders", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def create_order(
    order: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Создать новый заказ
    
    Требует JWT токен. Автоматически резервирует заказ на 30 минут.
    
    - **delivery_address**: Адрес доставки (обязательно)
    - **delivery_service**: Служба доставки (по умолчанию "Почта РФ")
    - **delivery_price**: Стоимость доставки (валидируется)
    - **items**: Список товаров в заказе (обязательно, не пустой)
    """
    if not order.items:
        raise ValidationError("Заказ должен содержать хотя бы один товар")
    
    # Валидация
    validate_price(order.delivery_price, min_price=0.0)
    
    # Вычисляем общую сумму
    total_amount = sum(item.price * item.quantity for item in order.items)
    total_amount += order.delivery_price
    
    # Проверяем товары и валидируем
    for item in order.items:
        validate_quantity(item.quantity, min_quantity=1)
        validate_price(item.price, min_price=0.0)
        
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise NotFoundError(f"Товар с ID {item.product_id}")
        if not product.is_available:
            raise ValidationError(f"Товар {product.name} недоступен")
    
    # Генерируем уникальный номер заказа
    order_number = generate_order_number()
    while db.query(Order).filter(Order.order_number == order_number).first():
        order_number = generate_order_number()
    
    try:
        # Создаем заказ
        new_order = Order(
            order_number=order_number,
            user_id=current_user.id,
            status="new",
            total_amount=total_amount,
            delivery_price=order.delivery_price,
            delivery_address=order.delivery_address,
            delivery_service=order.delivery_service,
            reserved_until=datetime.utcnow() + timedelta(minutes=30)
        )
        db.add(new_order)
        db.flush()  # Получаем ID заказа
        
        # Создаем элементы заказа
        for item in order.items:
            order_item = OrderItem(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            db.add(order_item)
        
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при создании заказа: {str(e)}")


@router.put("/orders/{order_id}", response_model=OrderSchema)
async def update_order(
    order_id: int,
    order_update: OrderUpdate,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Обновить заказ
    
    Пользователь может обновлять только свои заказы.
    Можно обновить статус, трекинг-номер, адрес доставки.
    
    - **order_id**: ID заказа
    - **status**: Новый статус (валидируется)
    - **tracking_number**: Трекинг-номер (опционально)
    - **delivery_address**: Адрес доставки (опционально)
    - **delivery_service**: Служба доставки (опционально)
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Проверяем права доступа
    if current_user and order.user_id != current_user.id:
        raise ForbiddenError("Можно обновлять только свои заказы")
    
    # Валидация
    update_data = order_update.dict(exclude_unset=True)
    
    if "status" in update_data:
        validate_order_status(update_data["status"])
    
    try:
        for field, value in update_data.items():
            setattr(order, field, value)
        
        db.commit()
        db.refresh(order)
        return order
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при обновлении заказа: {str(e)}")


@router.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Удалить заказ
    
    Пользователь может удалить только свои заказы.
    Можно удалить только заказы со статусом "new".
    
    - **order_id**: ID заказа
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Проверяем права доступа
    if order.user_id != current_user.id:
        raise ForbiddenError("Можно удалять только свои заказы")
    
    # Можно удалять только новые заказы
    if order.status != "new":
        raise ValidationError("Можно удалить только заказы со статусом 'new'")
    
    try:
        db.delete(order)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при удалении заказа: {str(e)}")
