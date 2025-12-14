"""
API endpoints для корзины с БД и JWT аутентификацией
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import CartItem, Product
from app.schemas.cart import CartItem as CartItemSchema, CartItemCreate
from app.auth import get_current_user
from app.models import User
from app.exceptions import NotFoundError, ValidationError, DatabaseError
from app.validators import validate_quantity

router = APIRouter()


@router.get("/cart", response_model=List[CartItemSchema])
async def get_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Получить корзину текущего пользователя
    
    Требует JWT токен в заголовке Authorization: Bearer <token>
    """
    cart_items = db.query(CartItem).filter(
        CartItem.user_id == current_user.id
    ).all()
    return cart_items


@router.post("/cart/items", response_model=CartItemSchema, status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    item: CartItemCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Добавить товар в корзину
    
    Если товар уже есть в корзине, увеличивает количество.
    
    - **product_id**: ID товара (обязательно)
    - **quantity**: Количество (обязательно, валидируется)
    """
    # Валидация
    validate_quantity(item.quantity, min_quantity=1)
    
    # Проверяем существование товара
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        raise NotFoundError("Товар")
    
    if not product.is_available:
        raise ValidationError("Товар недоступен")
    
    # Проверяем, есть ли уже такой товар в корзине
    existing_item = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.product_id == item.product_id
    ).first()
    
    if existing_item:
        # Увеличиваем количество
        try:
            existing_item.quantity += item.quantity
            validate_quantity(existing_item.quantity)
            db.commit()
            db.refresh(existing_item)
            return existing_item
        except Exception as e:
            db.rollback()
            raise DatabaseError(f"Ошибка при обновлении корзины: {str(e)}")
    else:
        # Создаем новый элемент корзины
        try:
            new_item = CartItem(
                user_id=current_user.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            return new_item
        except Exception as e:
            db.rollback()
            raise DatabaseError(f"Ошибка при добавлении в корзину: {str(e)}")


@router.put("/cart/items/{item_id}", response_model=CartItemSchema)
async def update_cart_item(
    item_id: int,
    quantity: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Обновить количество товара в корзине
    
    - **item_id**: ID элемента корзины
    - **quantity**: Новое количество (валидируется)
    """
    # Валидация
    validate_quantity(quantity, min_quantity=1)
    
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not item:
        raise NotFoundError("Товар в корзине")
    
    try:
        item.quantity = quantity
        db.commit()
        db.refresh(item)
        return item
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при обновлении корзины: {str(e)}")


@router.delete("/cart/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_cart(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Удалить товар из корзины
    
    - **item_id**: ID элемента корзины
    """
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not item:
        raise NotFoundError("Товар в корзине")
    
    try:
        db.delete(item)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при удалении из корзины: {str(e)}")


@router.delete("/cart", status_code=status.HTTP_204_NO_CONTENT)
async def clear_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Очистить корзину текущего пользователя
    """
    try:
        db.query(CartItem).filter(
            CartItem.user_id == current_user.id
        ).delete()
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при очистке корзины: {str(e)}")
