#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для быстрого тестирования API endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(method, url, data=None, headers=None, expected_status=200):
    """Тестирование endpoint"""
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        
        status_ok = response.status_code == expected_status
        status_icon = "✅" if status_ok else "❌"
        print(f"{status_icon} {method} {url} - {response.status_code} (ожидалось {expected_status})")
        
        if not status_ok:
            print(f"   Ответ: {response.text[:200]}")
        
        return response
    except requests.exceptions.ConnectionError:
        print(f"❌ {method} {url} - Сервер не запущен!")
        return None
    except Exception as e:
        print(f"❌ {method} {url} - Ошибка: {e}")
        return None

def main():
    print("=" * 60)
    print("Тестирование API endpoints")
    print("=" * 60)
    print("\n⚠️  Убедитесь, что сервер запущен: uvicorn main:app --reload")
    print()
    
    # Проверка health check
    print("1. Health check:")
    test_endpoint("GET", f"{BASE_URL}/health")
    
    # Проверка корневого endpoint
    print("\n2. Root endpoint:")
    test_endpoint("GET", f"{BASE_URL}/")
    
    # Проверка получения товаров
    print("\n3. Получение списка товаров:")
    test_endpoint("GET", f"{BASE_URL}/api/v1/products")
    
    # Проверка поиска товаров
    print("\n4. Поиск товаров:")
    test_endpoint("GET", f"{BASE_URL}/api/v1/products/search?q=сумка")
    
    # Проверка регистрации пользователя
    print("\n5. Регистрация пользователя:")
    register_data = {
        "phone_or_email": "test@example.com",
        "password": "test123456",
        "full_name": "Test User"
    }
    register_response = test_endpoint("POST", f"{BASE_URL}/api/v1/users/register", 
                                     data=register_data, expected_status=201)
    
    # Если регистрация успешна, пробуем войти
    if register_response and register_response.status_code == 201:
        print("\n6. Вход пользователя:")
        login_data = {
            "phone_or_email": "test@example.com",
            "password": "test123456"
        }
        login_response = test_endpoint("POST", f"{BASE_URL}/api/v1/users/login", 
                                data=login_data, expected_status=200)
        
        if login_response and login_response.status_code == 200:
            token = login_response.json().get("access_token")
            if token:
                headers = {"Authorization": f"Bearer {token}"}
                
                print("\n7. Получение текущего пользователя:")
                test_endpoint("GET", f"{BASE_URL}/api/v1/users/me", headers=headers)
                
                print("\n8. Получение корзины:")
                test_endpoint("GET", f"{BASE_URL}/api/v1/cart", headers=headers)
    
    print("\n" + "=" * 60)
    print("Тестирование завершено!")
    print("=" * 60)

if __name__ == "__main__":
    main()

