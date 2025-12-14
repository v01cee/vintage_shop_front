"""
Unit и Integration тесты для Users API
"""
import pytest
from fastapi import status


def test_register_user(client):
    """Тест регистрации пользователя"""
    response = client.post(
        "/api/v1/users/register",
        json={
            "phone_or_email": "newuser@example.com",
            "password": "password123",
            "full_name": "New User"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["phone_or_email"] == "newuser@example.com"
    assert data["full_name"] == "New User"
    assert "password_hash" not in data


def test_register_duplicate_user(client, test_user):
    """Тест регистрации с существующим email"""
    response = client.post(
        "/api/v1/users/register",
        json={
            "phone_or_email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == status.HTTP_409_CONFLICT


def test_register_invalid_email(client):
    """Тест регистрации с невалидным email"""
    response = client.post(
        "/api/v1/users/register",
        json={
            "phone_or_email": "invalid-email",
            "password": "password123"
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_register_short_password(client):
    """Тест регистрации с коротким паролем"""
    response = client.post(
        "/api/v1/users/register",
        json={
            "phone_or_email": "user@example.com",
            "password": "12345"  # Меньше 6 символов
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login_success(client, test_user):
    """Тест успешного входа"""
    response = client.post(
        "/api/v1/users/login",
        data={
            "username": "test@example.com",  # OAuth2 использует username
            "password": "password123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "user" in data


def test_login_wrong_password(client, test_user):
    """Тест входа с неверным паролем"""
    response = client.post(
        "/api/v1/users/login",
        data={
            "username": "test@example.com",  # OAuth2 использует username
            "password": "wrongpassword"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_current_user(client, auth_headers):
    """Тест получения текущего пользователя"""
    response = client.get("/api/v1/users/me", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "id" in data
    assert "phone_or_email" in data


def test_get_current_user_unauthorized(client):
    """Тест получения текущего пользователя без токена"""
    response = client.get("/api/v1/users/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_update_user(client, test_user, auth_headers):
    """Тест обновления пользователя"""
    response = client.put(
        f"/api/v1/users/{test_user.id}",
        json={
            "full_name": "Updated Name",
            "phone": "+79991234567"
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["full_name"] == "Updated Name"
    assert data["phone"] == "+79991234567"


def test_update_other_user(client, test_user, auth_headers):
    """Тест обновления чужого пользователя"""
    # Создаем другого пользователя
    response = client.post(
        "/api/v1/users/register",
        json={
            "phone_or_email": "other@example.com",
            "password": "password123"
        }
    )
    other_user_id = response.json()["id"]
    
    # Пытаемся обновить его данные
    response = client.put(
        f"/api/v1/users/{other_user_id}",
        json={"full_name": "Hacked"},
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
