"""
API endpoints для товаров с БД
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List
from app.database import get_db
from app.models import Product, User
from app.schemas.product import Product as ProductSchema, ProductCreate, ProductUpdate
from app.exceptions import NotFoundError, ValidationError, DatabaseError
from app.validators import validate_price, validate_quantity
from app.auth import get_current_admin

router = APIRouter()


@router.get("/products", response_model=List[ProductSchema])
async def get_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    category: str = Query(None),
    is_available: bool = Query(None),
    db: Session = Depends(get_db)
):
    """
    Получить список товаров
    
    - **skip**: Количество пропущенных записей (для пагинации)
    - **limit**: Максимальное количество записей (1-1000)
    - **category**: Фильтр по категории (опционально)
    - **is_available**: Фильтр по доступности (опционально)
    """
    query = db.query(Product)
    
    if category:
        query = query.filter(Product.category == category)
    
    if is_available is not None:
        query = query.filter(Product.is_available == is_available)
    
    products = query.offset(skip).limit(limit).all()
    return products


@router.get("/products/search", response_model=List[ProductSchema])
async def search_products(
    q: str = Query(..., min_length=1, description="Поисковый запрос"),
    db: Session = Depends(get_db)
):
    """
    Поиск товаров по названию, описанию или артикулу
    
    - **q**: Поисковый запрос (минимум 1 символ)
    """
    search_term = f"%{q.lower()}%"
    products = db.query(Product).filter(
        or_(
            Product.name.ilike(search_term),
            Product.description.ilike(search_term),
            Product.article.ilike(search_term)
        )
    ).all()
    return products


@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Получить товар по ID
    
    Автоматически увеличивает счетчик просмотров.
    
    - **product_id**: ID товара
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise NotFoundError("Товар")
    
    # Увеличиваем счетчик просмотров
    try:
        product.views = (product.views or 0) + 1
        db.commit()
        db.refresh(product)
    except Exception as e:
        db.rollback()
        # Не прерываем выполнение, если не удалось обновить просмотры
    
    return product


@router.post("/products", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Создать новый товар
    
    Требует права администратора.
    
    - **name**: Название товара (обязательно)
    - **price**: Цена от поставщика (обязательно, валидируется)
    - **boutique_price**: Цена в бутиках (опционально)
    - **article**: Артикул товара (опционально)
    - **quantity**: Количество на складе (по умолчанию 1, валидируется)
    - **category**: Категория (опционально)
    - **description**: Описание (опционально)
    - **image**: Главное изображение URL (опционально)
    - **images**: Список дополнительных изображений (опционально)
    - **tags**: Список тегов (опционально)
    - **is_available**: Доступен ли товар (по умолчанию True)
    """
    # Валидация
    validate_price(product.price)
    if product.boutique_price:
        validate_price(product.boutique_price)
    validate_quantity(product.quantity or 1)
    
    try:
        new_product = Product(**product.dict())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при создании товара: {str(e)}")


@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(
    product_id: int,
    product: ProductUpdate,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Обновить товар
    
    Требует права администратора.
    
    - **product_id**: ID товара
    - Можно обновить любые поля из ProductUpdate
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise NotFoundError("Товар")
    
    # Валидация обновляемых полей
    update_data = product.dict(exclude_unset=True)
    
    if "price" in update_data:
        validate_price(update_data["price"])
    if "boutique_price" in update_data and update_data["boutique_price"]:
        validate_price(update_data["boutique_price"])
    if "quantity" in update_data:
        validate_quantity(update_data["quantity"])
    
    try:
        for field, value in update_data.items():
            setattr(db_product, field, value)
        
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при обновлении товара: {str(e)}")


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Удалить товар
    
    Требует права администратора.
    
    - **product_id**: ID товара
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise NotFoundError("Товар")
    
    try:
        db.delete(product)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при удалении товара: {str(e)}")
