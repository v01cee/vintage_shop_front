from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.cart import CartItem, CartItemCreate

router = APIRouter()

# Временное хранилище корзины (в сессии или БД)
carts_db = {}


@router.get("/cart/{user_id}", response_model=List[CartItem])
async def get_cart(user_id: str = "default"):
    """Получить корзину пользователя"""
    return carts_db.get(user_id, [])


@router.post("/cart/{user_id}/items", response_model=CartItem, status_code=201)
async def add_to_cart(user_id: str, item: CartItemCreate):
    """Добавить товар в корзину"""
    if user_id not in carts_db:
        carts_db[user_id] = []
    
    # Проверяем, есть ли уже такой товар в корзине
    existing_item = next(
        (i for i in carts_db[user_id] if i["product_id"] == item.product_id),
        None
    )
    
    if existing_item:
        existing_item["quantity"] += item.quantity
        return existing_item
    else:
        new_item = {
            "id": len(carts_db[user_id]) + 1,
            "product_id": item.product_id,
            "quantity": item.quantity
        }
        carts_db[user_id].append(new_item)
        return new_item


@router.put("/cart/{user_id}/items/{item_id}", response_model=CartItem)
async def update_cart_item(user_id: str, item_id: int, quantity: int):
    """Обновить количество товара в корзине"""
    if user_id not in carts_db:
        raise HTTPException(status_code=404, detail="Корзина не найдена")
    
    item = next((i for i in carts_db[user_id] if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Товар в корзине не найден")
    
    item["quantity"] = quantity
    return item


@router.delete("/cart/{user_id}/items/{item_id}", status_code=204)
async def remove_from_cart(user_id: str, item_id: int):
    """Удалить товар из корзины"""
    if user_id not in carts_db:
        raise HTTPException(status_code=404, detail="Корзина не найдена")
    
    item_index = next((i for i, item in enumerate(carts_db[user_id]) if item["id"] == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Товар в корзине не найден")
    
    carts_db[user_id].pop(item_index)
    return None


@router.delete("/cart/{user_id}", status_code=204)
async def clear_cart(user_id: str):
    """Очистить корзину"""
    if user_id in carts_db:
        carts_db[user_id] = []
    return None

