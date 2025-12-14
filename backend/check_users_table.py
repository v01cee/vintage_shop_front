#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для проверки содержимого таблицы users
"""
from sqlalchemy import create_engine, inspect, text

# Захардкоженный DATABASE_URL (временно)
DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"

engine = create_engine(DATABASE_URL)

def check_users():
    """Проверка содержимого таблицы users"""
    print("=" * 60)
    print("Проверка содержимого таблицы users")
    print("=" * 60)
    
    with engine.connect() as conn:
        # Проверяем количество записей
        result = conn.execute(text("SELECT COUNT(*) FROM users;"))
        count = result.scalar()
        print(f"\nВсего записей в таблице users: {count}")
        
        if count == 0:
            print("\n[OK] Таблица пуста, можно регистрировать новых пользователей")
            return
        
        # Получаем все записи
        print("\nВсе записи в таблице users:")
        print("-" * 60)
        
        result = conn.execute(text("""
            SELECT 
                id, 
                phone_or_email, 
                full_name, 
                phone, 
                address,
                created_at
            FROM users 
            ORDER BY id;
        """))
        
        rows = result.fetchall()
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"  phone_or_email: {row[1]}")
            print(f"  full_name: {row[2]}")
            print(f"  phone: {row[3]}")
            print(f"  address: {row[4]}")
            print(f"  created_at: {row[5]}")
            print("-" * 60)
        
        # Проверяем конкретный email/телефон
        test_email = "test@example.com"
        print(f"\nПроверка наличия '{test_email}':")
        result = conn.execute(
            text("SELECT id, phone_or_email FROM users WHERE phone_or_email = :email"),
            {"email": test_email}
        )
        found = result.fetchone()
        if found:
            print(f"[FOUND] Найден пользователь с ID {found[0]}, phone_or_email: {found[1]}")
        else:
            print(f"[NOT FOUND] Пользователь с '{test_email}' не найден")
        
        # Проверяем NULL значения
        print("\nПроверка записей с NULL в phone_or_email:")
        result = conn.execute(text("SELECT COUNT(*) FROM users WHERE phone_or_email IS NULL;"))
        null_count = result.scalar()
        if null_count > 0:
            print(f"[WARN] Найдено {null_count} записей с NULL в phone_or_email")
            print("Это может вызывать проблемы с уникальным индексом")
        else:
            print("[OK] Нет записей с NULL в phone_or_email")

if __name__ == "__main__":
    try:
        check_users()
    except Exception as e:
        print(f"\n[FAIL] Ошибка: {e}")
        import traceback
        traceback.print_exc()

