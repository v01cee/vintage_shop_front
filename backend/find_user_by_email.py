#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для поиска пользователя по email/телефону
"""
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
engine = create_engine(DATABASE_URL)

def find_user(email):
    """Поиск пользователя по email"""
    print(f"Поиск пользователя с phone_or_email = '{email}'")
    print("=" * 60)
    
    with engine.connect() as conn:
        # Точное совпадение
        result = conn.execute(
            text("SELECT * FROM users WHERE phone_or_email = :email"),
            {"email": email}
        )
        found = result.fetchone()
        
        if found:
            print(f"[FOUND] Найден пользователь:")
            print(f"  ID: {found[0]}")
            print(f"  phone_or_email: {found[1]}")
            print(f"  password_hash: {found[2][:20]}...")
            print(f"  full_name: {found[3]}")
            print(f"  phone: {found[4]}")
            print(f"  address: {found[5]}")
            print(f"  created_at: {found[6]}")
            print(f"  updated_at: {found[7]}")
        else:
            print(f"[NOT FOUND] Пользователь с '{email}' не найден")
        
        # Проверяем case-insensitive
        print(f"\nПоиск без учета регистра (ILIKE):")
        result = conn.execute(
            text("SELECT id, phone_or_email FROM users WHERE phone_or_email ILIKE :email"),
            {"email": email}
        )
        found_ilike = result.fetchall()
        if found_ilike:
            print(f"[FOUND] Найдено {len(found_ilike)} записей:")
            for row in found_ilike:
                print(f"  ID: {row[0]}, phone_or_email: {row[1]}")
        else:
            print(f"[NOT FOUND] Не найдено")
        
        # Показываем все записи с phone_or_email
        print(f"\nВсе записи с заполненным phone_or_email:")
        result = conn.execute(
            text("SELECT id, phone_or_email, full_name FROM users WHERE phone_or_email IS NOT NULL ORDER BY id")
        )
        all_users = result.fetchall()
        if all_users:
            for row in all_users:
                print(f"  ID: {row[0]}, phone_or_email: {row[1]}, full_name: {row[2]}")
        else:
            print("  [EMPTY] Нет записей с заполненным phone_or_email")

if __name__ == "__main__":
    import sys
    email = sys.argv[1] if len(sys.argv) > 1 else "test@example.com"
    find_user(email)



