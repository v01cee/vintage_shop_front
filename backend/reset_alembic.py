#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для сброса состояния Alembic миграций
Используйте если возникли проблемы с миграциями
"""
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("Ошибка: DATABASE_URL не найден в .env файле")
    exit(1)

engine = create_engine(DATABASE_URL)

print("Подключение к базе данных...")
with engine.connect() as conn:
    # Проверяем, существует ли таблица alembic_version
    result = conn.execute(text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'alembic_version'
        );
    """))
    exists = result.scalar()
    
    if exists:
        # Получаем текущую версию
        result = conn.execute(text("SELECT version_num FROM alembic_version"))
        current_version = result.scalar()
        print(f"Текущая версия в БД: {current_version}")
        
        # Удаляем таблицу alembic_version
        conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
        conn.commit()
        print("Таблица alembic_version удалена")
    else:
        print("Таблица alembic_version не существует")
    
    print("\nТеперь можно применить миграцию командой:")
    print("alembic upgrade head")

