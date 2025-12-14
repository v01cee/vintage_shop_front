"""
Unit и Integration тесты для Products API
"""
import pytest
from fastapi import status


def test_get_products(client, test_product):
    """Тест получения списка товаров"""
    response = client.get("/api/v1/products")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_product_by_id(client, test_product):
    """Тест получения товара по ID"""
    response = client.get(f"/api/v1/products/{test_product.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == test_product.id
    assert data["name"] == test_product.name


def test_get_product_not_found(client):
    """Тест получения несуществующего товара"""
    response = client.get("/api/v1/products/99999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_search_products(client, test_product):
    """Тест поиска товаров"""
    response = client.get("/api/v1/products/search?q=Test")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_create_product_as_admin(client, admin_headers):
    """Тест создания товара администратором"""
    response = client.post(
        "/api/v1/products",
        json={
            "name": "New Product",
            "description": "New Description",
            "price": 2000.0,
            "quantity": 5,
            "is_available": True
        },
        headers=admin_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "New Product"
    assert data["price"] == 2000.0


def test_create_product_unauthorized(client, auth_headers):
    """Тест создания товара обычным пользователем (должно быть запрещено)"""
    response = client.post(
        "/api/v1/products",
        json={
            "name": "New Product",
            "price": 2000.0,
            "quantity": 5
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_create_product_negative_price(client, admin_headers):
    """Тест создания товара с отрицательной ценой"""
    response = client.post(
        "/api/v1/products",
        json={
            "name": "Product",
            "price": -100.0,
            "quantity": 1
        },
        headers=admin_headers
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_update_product_as_admin(client, test_product, admin_headers):
    """Тест обновления товара администратором"""
    response = client.put(
        f"/api/v1/products/{test_product.id}",
        json={
            "name": "Updated Product",
            "price": 1500.0
        },
        headers=admin_headers
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["price"] == 1500.0


def test_update_product_unauthorized(client, test_product, auth_headers):
    """Тест обновления товара обычным пользователем (должно быть запрещено)"""
    response = client.put(
        f"/api/v1/products/{test_product.id}",
        json={
            "name": "Updated Product",
            "price": 1500.0
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_delete_product_as_admin(client, test_product, admin_headers):
    """Тест удаления товара администратором"""
    response = client.delete(
        f"/api/v1/products/{test_product.id}",
        headers=admin_headers
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Проверяем, что товар удален
    response = client.get(f"/api/v1/products/{test_product.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_product_unauthorized(client, test_product, auth_headers):
    """Тест удаления товара обычным пользователем (должно быть запрещено)"""
    response = client.delete(
        f"/api/v1/products/{test_product.id}",
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
