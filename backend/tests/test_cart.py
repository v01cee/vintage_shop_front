"""
Integration тесты для Cart API
"""
import pytest
from fastapi import status


def test_get_cart_empty(client, auth_headers):
    """Тест получения пустой корзины"""
    response = client.get("/api/v1/cart", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_add_to_cart(client, test_product, auth_headers):
    """Тест добавления товара в корзину"""
    response = client.post(
        "/api/v1/cart/items",
        json={
            "product_id": test_product.id,
            "quantity": 2
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["product_id"] == test_product.id
    assert data["quantity"] == 2


def test_add_to_cart_unauthorized(client, test_product):
    """Тест добавления в корзину без авторизации"""
    response = client.post(
        "/api/v1/cart/items",
        json={
            "product_id": test_product.id,
            "quantity": 1
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_update_cart_item(client, test_product, auth_headers):
    """Тест обновления количества товара в корзине"""
    # Добавляем товар
    response = client.post(
        "/api/v1/cart/items",
        json={
            "product_id": test_product.id,
            "quantity": 1
        },
        headers=auth_headers
    )
    item_id = response.json()["id"]
    
    # Обновляем количество
    response = client.put(
        f"/api/v1/cart/items/{item_id}",
        params={"quantity": 5},
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["quantity"] == 5


def test_remove_from_cart(client, test_product, auth_headers):
    """Тест удаления товара из корзины"""
    # Добавляем товар
    response = client.post(
        "/api/v1/cart/items",
        json={
            "product_id": test_product.id,
            "quantity": 1
        },
        headers=auth_headers
    )
    item_id = response.json()["id"]
    
    # Удаляем товар
    response = client.delete(
        f"/api/v1/cart/items/{item_id}",
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_clear_cart(client, test_product, auth_headers):
    """Тест очистки корзины"""
    # Добавляем товар
    client.post(
        "/api/v1/cart/items",
        json={
            "product_id": test_product.id,
            "quantity": 1
        },
        headers=auth_headers
    )
    
    # Очищаем корзину
    response = client.delete("/api/v1/cart", headers=auth_headers)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Проверяем, что корзина пуста
    response = client.get("/api/v1/cart", headers=auth_headers)
    assert len(response.json()) == 0
