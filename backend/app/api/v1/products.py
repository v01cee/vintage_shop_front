from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.product import Product, ProductCreate, ProductUpdate

router = APIRouter()

# Временные данные для разработки (потом заменим на БД)
products_db = [
    {
        "id": 1,
        "name": "Винтажная сумка",
        "description": "Красивая винтажная сумка из кожи",
        "price": 5000,
        "image": "",
        "category": "Аксессуары"
    },
    {
        "id": 2,
        "name": "Винтажное платье",
        "description": "Элегантное платье 80-х годов",
        "price": 8000,
        "image": "",
        "category": "Одежда"
    },
    {
        "id": 3,
        "name": "Винтажные духи",
        "description": "Редкие духи из коллекции",
        "price": 12000,
        "image": "",
        "category": "Парфюмерия"
    },
    {
        "id": 4,
        "name": "Винтажные часы",
        "description": "Швейцарские часы 70-х",
        "price": 15000,
        "image": "",
        "category": "Аксессуары"
    },
    {
        "id": 5,
        "name": "Винтажная куртка",
        "description": "Кожаная куртка в отличном состоянии",
        "price": 10000,
        "image": "",
        "category": "Одежда"
    },
    {
        "id": 6,
        "name": "Винтажная косметика",
        "description": "Ретро косметика из коллекции",
        "price": 3000,
        "image": "",
        "category": "Косметика"
    },
    {
        "id": 7,
        "name": "Винтажные очки",
        "description": "Стильные очки 90-х",
        "price": 4000,
        "image": "",
        "category": "Аксессуары"
    },
    {
        "id": 8,
        "name": "Винтажное украшение",
        "description": "Серебряное кольцо с камнем",
        "price": 6000,
        "image": "",
        "category": "Аксессуары"
    },
    {
        "id": 9,
        "name": "Винтажная блузка",
        "description": "Шелковая блузка в винтажном стиле",
        "price": 4500,
        "image": "",
        "category": "Одежда"
    },
    {
        "id": 10,
        "name": "Винтажный парфюм",
        "description": "Классический аромат",
        "price": 7000,
        "image": "",
        "category": "Парфюмерия"
    }
]


@router.get("/products", response_model=List[Product])
async def get_products(skip: int = 0, limit: int = 100):
    """Получить список всех товаров"""
    return products_db[skip:skip + limit]


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Получить товар по ID"""
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


@router.post("/products", response_model=Product, status_code=201)
async def create_product(product: ProductCreate):
    """Создать новый товар"""
    new_id = max([p["id"] for p in products_db], default=0) + 1
    new_product = {
        "id": new_id,
        **product.dict()
    }
    products_db.append(new_product)
    return new_product


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate):
    """Обновить товар"""
    product_index = next((i for i, p in enumerate(products_db) if p["id"] == product_id), None)
    if product_index is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    updated_product = {**products_db[product_index], **product.dict(exclude_unset=True)}
    products_db[product_index] = updated_product
    return updated_product


@router.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    """Удалить товар"""
    product_index = next((i for i, p in enumerate(products_db) if p["id"] == product_id), None)
    if product_index is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    products_db.pop(product_index)
    return None

