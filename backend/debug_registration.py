#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для отладки проблемы с регистрацией
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models import User

DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def test_query():
    """Тестирование запроса как в коде"""
    db = SessionLocal()
    try:
        email = "test@example.com"
        print(f"Поиск пользователя с phone_or_email = '{email}'")
        
        # Точно как в коде
        existing_user = db.query(User).filter(
            User.phone_or_email == email
        ).first()
        
        if existing_user:
            print(f"[FOUND] Найден: ID={existing_user.id}, phone_or_email={existing_user.phone_or_email}")
        else:
            print(f"[NOT FOUND] Пользователь не найден")
        
        # Проверяем через raw SQL
        result = db.execute(text("SELECT id, phone_or_email FROM users WHERE phone_or_email = :email"), {"email": email})
        raw_result = result.fetchone()
        if raw_result:
            print(f"[RAW SQL FOUND] Найден: ID={raw_result[0]}, phone_or_email={raw_result[1]}")
        else:
            print(f"[RAW SQL NOT FOUND] Пользователь не найден")
        
        # Проверяем все записи
        all_users = db.query(User).all()
        print(f"\nВсего пользователей через ORM: {len(all_users)}")
        for u in all_users:
            print(f"  ID: {u.id}, phone_or_email: {u.phone_or_email}")
        
    finally:
        db.close()

if __name__ == "__main__":
    test_query()

