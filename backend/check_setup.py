#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для проверки установки зависимостей и готовности к запуску
"""
import sys

def check_module(module_name, package_name=None):
    """Проверка наличия модуля"""
    try:
        __import__(module_name)
        print(f"[OK] {module_name}")
        return True
    except ImportError:
        pkg = package_name or module_name
        print(f"[FAIL] {module_name} - установите: pip install {pkg}")
        return False

print("Проверка зависимостей...")
print("=" * 60)

modules = [
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn[standard]"),
    ("sqlalchemy", "sqlalchemy"),
    ("alembic", "alembic"),
    ("pydantic", "pydantic"),
    ("jose", "python-jose[cryptography]"),
    ("passlib", "passlib[bcrypt]"),
    ("dotenv", "python-dotenv"),
    ("psycopg2", "psycopg2-binary"),
    ("pytest", "pytest"),
    ("httpx", "httpx"),
]

all_ok = True
for module, package in modules:
    if not check_module(module, package):
        all_ok = False

print("=" * 60)

if all_ok:
    print("\n[OK] Все зависимости установлены!")
    print("\nМожно запускать:")
    print("1. Сервер: uvicorn main:app --reload")
    print("2. Тесты: pytest tests/ -v")
else:
    print("\n[FAIL] Некоторые зависимости отсутствуют!")
    print("\nУстановите зависимости:")
    print("pip install -r requirements.txt")
    sys.exit(1)

# Проверка подключения к БД
print("\n" + "=" * 60)
print("Проверка подключения к БД...")
print("=" * 60)

try:
    from app.database import engine
    with engine.connect() as conn:
        print("[OK] Подключение к БД успешно!")
        print(f"   База данных: {engine.url.database}")
        print(f"   Хост: {engine.url.host}")
        print(f"   Порт: {engine.url.port}")
except Exception as e:
    print(f"[FAIL] Ошибка подключения к БД: {e}")
    print("   Проверьте файл .env и настройки DATABASE_URL")

print("\n" + "=" * 60)



