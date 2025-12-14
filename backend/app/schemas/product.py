from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float  # Цена от поставщика
    boutique_price: Optional[float] = None  # Цена в бутиках
    article: Optional[str] = None  # Артикул товара
    quantity: int = 1  # Количество на складе
    views: int = 0  # Количество просмотров
    category: Optional[str] = None
    image: Optional[str] = None  # Главное изображение
    images: Optional[List[str]] = None  # Дополнительные изображения
    tags: Optional[List[str]] = None  # Теги/характеристики
    is_available: bool = True  # Доступен ли товар


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    boutique_price: Optional[float] = None
    article: Optional[str] = None
    quantity: Optional[int] = None
    views: Optional[int] = None
    category: Optional[str] = None
    image: Optional[str] = None
    images: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    is_available: Optional[bool] = None


class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

