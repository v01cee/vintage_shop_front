"""
Unit и Integration тесты для Orders API
"""
import pytest
from fastapi import status


def test_get_orders_empty(client, auth_headers):
    """Тест получения пустого списка заказов"""
    response = client.get("/api/v1/orders", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)


def test_create_order(client, auth_headers, test_product):
    """Тест создания заказа"""
    response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "delivery_service": "Почта РФ",
            "delivery_price": 300.0,
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 2,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "order_number" in data
    assert data["status"] == "new"
    assert data["total_amount"] == test_product.price * 2 + 300.0
    assert len(data["items"]) == 1


def test_create_order_empty_items(client, auth_headers):
    """Тест создания заказа без товаров"""
    response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": []
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_order_by_id(client, auth_headers, test_product):
    """Тест получения заказа по ID"""
    # Создаем заказ
    create_response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 1,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    order_id = create_response.json()["id"]
    
    # Получаем заказ
    response = client.get(f"/api/v1/orders/{order_id}", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == order_id
    assert "order_number" in data


def test_get_order_not_found(client, auth_headers):
    """Тест получения несуществующего заказа"""
    response = client.get("/api/v1/orders/99999", headers=auth_headers)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_order_status(client, auth_headers, test_product):
    """Тест обновления статуса заказа"""
    # Создаем заказ
    create_response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 1,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    order_id = create_response.json()["id"]
    
    # Обновляем статус
    response = client.put(
        f"/api/v1/orders/{order_id}",
        json={"status": "paid"},
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["status"] == "paid"


def test_update_order_invalid_status(client, auth_headers, test_product):
    """Тест обновления заказа с невалидным статусом"""
    # Создаем заказ
    create_response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 1,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    order_id = create_response.json()["id"]
    
    # Пытаемся обновить с невалидным статусом
    response = client.put(
        f"/api/v1/orders/{order_id}",
        json={"status": "invalid_status"},
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_search_order_by_number(client, auth_headers, test_product):
    """Тест поиска заказа по номеру"""
    # Создаем заказ
    create_response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 1,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    order_number = create_response.json()["order_number"]
    
    # Ищем заказ по номеру
    response = client.get(f"/api/v1/orders/search/{order_number}", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["order_number"] == order_number


def test_get_orders_with_status_filter(client, auth_headers, test_product):
    """Тест получения заказов с фильтром по статусу"""
    # Создаем заказ
    create_response = client.post(
        "/api/v1/orders",
        json={
            "delivery_address": "г. Москва, ул. Тестовая, д. 1",
            "items": [
                {
                    "product_id": test_product.id,
                    "quantity": 1,
                    "price": test_product.price
                }
            ]
        },
        headers=auth_headers
    )
    order_id = create_response.json()["id"]
    
    # Обновляем статус на "paid"
    client.put(
        f"/api/v1/orders/{order_id}",
        json={"status": "paid"},
        headers=auth_headers
    )
    
    # Фильтруем по статусу "paid"
    response = client.get("/api/v1/orders?status=paid", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert all(order["status"] == "paid" for order in data)
