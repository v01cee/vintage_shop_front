"""
Unit и Integration тесты для Reviews API
"""
import pytest
from fastapi import status


def test_get_reviews_empty(client):
    """Тест получения пустого списка отзывов"""
    response = client.get("/api/v1/reviews")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)


def test_create_review(client, auth_headers, test_product):
    """Тест создания отзыва"""
    response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Отличный товар! Очень доволен покупкой.",
            "images": []
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["product_id"] == test_product.id
    assert "Отличный товар" in data["text"]
    assert "id" in data


def test_create_review_duplicate(client, auth_headers, test_product):
    """Тест создания дублирующего отзыва"""
    # Создаем первый отзыв
    client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Первый отзыв"
        },
        headers=auth_headers
    )
    
    # Пытаемся создать второй отзыв на тот же товар
    response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Второй отзыв"
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_409_CONFLICT


def test_create_review_empty_text(client, auth_headers, test_product):
    """Тест создания отзыва с пустым текстом"""
    response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "   "  # Только пробелы
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_review_by_id(client, auth_headers, test_product):
    """Тест получения отзыва по ID"""
    # Создаем отзыв
    create_response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Тестовый отзыв"
        },
        headers=auth_headers
    )
    review_id = create_response.json()["id"]
    
    # Получаем отзыв
    response = client.get(f"/api/v1/reviews/{review_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == review_id
    assert data["product_id"] == test_product.id


def test_get_review_not_found(client):
    """Тест получения несуществующего отзыва"""
    response = client.get("/api/v1/reviews/99999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_reviews_by_product_id(client, auth_headers, test_product):
    """Тест получения отзывов по ID товара"""
    # Создаем отзыв
    client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Отзыв на товар"
        },
        headers=auth_headers
    )
    
    # Получаем отзывы для товара
    response = client.get(f"/api/v1/reviews?product_id={test_product.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert all(review["product_id"] == test_product.id for review in data)


def test_update_review_add_seller_response(client, auth_headers, test_product):
    """Тест обновления отзыва (добавление ответа продавца)"""
    # Создаем отзыв
    create_response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Отзыв"
        },
        headers=auth_headers
    )
    review_id = create_response.json()["id"]
    
    # Добавляем ответ продавца
    response = client.put(
        f"/api/v1/reviews/{review_id}",
        json={"seller_response": "Спасибо за отзыв!"},
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["seller_response"] == "Спасибо за отзыв!"


def test_create_review_unauthorized(client, test_product):
    """Тест создания отзыва без авторизации"""
    response = client.post(
        "/api/v1/reviews",
        json={
            "product_id": test_product.id,
            "text": "Отзыв"
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
