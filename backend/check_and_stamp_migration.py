#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для проверки существования таблиц и пометки миграции как примененной
Используйте если таблицы уже существуют в БД
"""
import os
from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("Ошибка: DATABASE_URL не найден в .env файле")
    exit(1)

engine = create_engine(DATABASE_URL)

# Список таблиц, которые должны быть созданы миграцией
required_tables = [
    'users',
    'products',
    'cart_items',
    'orders',
    'order_items',
    'order_comments',
    'reviews'
]

print("Проверка существования таблиц в базе данных...")
inspector = inspect(engine)
existing_tables = inspector.get_table_names()

print(f"\nСуществующие таблицы: {existing_tables}")

# Проверяем, какие таблицы уже существуют
missing_tables = []
for table in required_tables:
    if table in existing_tables:
        print(f"✅ Таблица '{table}' существует")
    else:
        print(f"❌ Таблица '{table}' отсутствует")
        missing_tables.append(table)

if missing_tables:
    print(f"\n⚠️  Отсутствуют таблицы: {missing_tables}")
    print("Нужно применить миграцию: alembic upgrade head")
else:
    print("\n✅ Все таблицы существуют!")
    
    # Проверяем alembic_version
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'alembic_version'
            );
        """))
        alembic_exists = result.scalar()
        
        if alembic_exists:
            result = conn.execute(text("SELECT version_num FROM alembic_version"))
            current_version = result.scalar()
            print(f"Текущая версия Alembic: {current_version}")
        else:
            print("\n⚠️  Таблица alembic_version не существует")
            print("Нужно пометить миграцию как примененную:")
            print("alembic stamp head")
            print("\nИли создать таблицу вручную:")
            print("""
CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version (version_num) VALUES ('0003');
            """)



