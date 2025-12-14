#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для тестирования регистрации пользователя
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_register(email, password, full_name=None):
    """Тест регистрации"""
    data = {
        "phone_or_email": email,
        "password": password
    }
    if full_name:
        data["full_name"] = full_name
    
    print(f"\nПопытка регистрации с email: {email}")
    response = requests.post(
        f"{BASE_URL}/api/v1/users/register",
        json=data
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 201:
        print("[OK] Регистрация успешна!")
        return response.json()
    elif response.status_code == 409:
        print("[FAIL] Пользователь уже существует")
        # Проверяем, что реально в БД
        check_db_for_email(email)
    else:
        print(f"[FAIL] Ошибка: {response.status_code}")
    
    return None

def check_db_for_email(email):
    """Проверка наличия email в БД"""
    from sqlalchemy import create_engine, text
    
    DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, phone_or_email, full_name FROM users WHERE phone_or_email = :email"),
            {"email": email}
        )
        found = result.fetchone()
        if found:
            print(f"[DB CHECK] Найден в БД: ID={found[0]}, phone_or_email={found[1]}, full_name={found[2]}")
        else:
            print(f"[DB CHECK] НЕ найден в БД - возможно проблема в коде проверки")

if __name__ == "__main__":
    print("=" * 60)
    print("Тестирование регистрации")
    print("=" * 60)
    
    # Тест 1: Новый пользователь
    test_register("test@example.com", "test123456", "Test User")
    
    # Тест 2: Попытка зарегистрировать того же пользователя
    test_register("test@example.com", "test123456", "Test User")

