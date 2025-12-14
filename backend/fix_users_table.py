#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для проверки и исправления структуры таблицы users
"""
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import ProgrammingError

# Захардкоженный DATABASE_URL (временно)
DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"

engine = create_engine(DATABASE_URL)

def check_table_structure():
    """Проверка структуры таблицы users"""
    inspector = inspect(engine)
    
    if 'users' not in inspector.get_table_names():
        print("[FAIL] Таблица 'users' не существует!")
        return False, []
    
    print("[OK] Таблица 'users' существует")
    
    # Получаем колонки
    columns = inspector.get_columns('users')
    column_names = [col['name'] for col in columns]
    
    print(f"\nТекущие колонки в таблице 'users':")
    for col in columns:
        print(f"  - {col['name']} ({col['type']})")
    
    # Проверяем наличие необходимых колонок
    required_columns = ['id', 'phone_or_email', 'password_hash', 'full_name', 'phone', 'address', 'created_at', 'updated_at']
    missing_columns = [col for col in required_columns if col not in column_names]
    
    if missing_columns:
        print(f"\n[FAIL] Отсутствуют колонки: {', '.join(missing_columns)}")
        return False, missing_columns
    else:
        print("\n[OK] Все необходимые колонки присутствуют")
        return True, []

def fix_users_table():
    """Исправление структуры таблицы users"""
    print("=" * 60)
    print("Проверка структуры таблицы users")
    print("=" * 60)
    
    result, missing = check_table_structure()
    
    if result:
        print("\n[OK] Структура таблицы корректна!")
        return
    
    if not missing:
        return
    
    print(f"\n{'=' * 60}")
    print("Исправление структуры таблицы")
    print("=" * 60)
    
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            # Добавляем недостающие колонки
            if 'phone_or_email' in missing:
                print("\nДобавляем колонку 'phone_or_email'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN phone_or_email VARCHAR(255);
                """))
                print("[OK] Колонка 'phone_or_email' добавлена")
            
            if 'password_hash' in missing:
                print("\nДобавляем колонку 'password_hash'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN password_hash VARCHAR(255);
                """))
                print("[OK] Колонка 'password_hash' добавлена")
            
            if 'full_name' in missing:
                print("\nДобавляем колонку 'full_name'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN full_name VARCHAR(255);
                """))
                print("[OK] Колонка 'full_name' добавлена")
            
            if 'phone' in missing:
                print("\nДобавляем колонку 'phone'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN phone VARCHAR(50);
                """))
                print("[OK] Колонка 'phone' добавлена")
            
            if 'address' in missing:
                print("\nДобавляем колонку 'address'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN address TEXT;
                """))
                print("[OK] Колонка 'address' добавлена")
            
            if 'created_at' in missing:
                print("\nДобавляем колонку 'created_at'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN created_at TIMESTAMP WITH TIME ZONE DEFAULT now();
                """))
                print("[OK] Колонка 'created_at' добавлена")
            
            if 'updated_at' in missing:
                print("\nДобавляем колонку 'updated_at'...")
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN updated_at TIMESTAMP WITH TIME ZONE DEFAULT now();
                """))
                print("[OK] Колонка 'updated_at' добавлена")
            
            # Создаем индексы
            print("\nСоздаем индексы...")
            try:
                conn.execute(text("CREATE INDEX IF NOT EXISTS ix_users_phone_or_email ON users(phone_or_email);"))
                print("[OK] Индекс на phone_or_email создан")
            except ProgrammingError as e:
                if "already exists" not in str(e).lower():
                    print(f"[WARN] Индекс уже существует или ошибка: {e}")
            
            trans.commit()
            print("\n" + "=" * 60)
            print("[OK] Структура таблицы исправлена!")
            print("=" * 60)
            
        except Exception as e:
            trans.rollback()
            print(f"\n[FAIL] Ошибка при исправлении: {e}")
            raise

if __name__ == "__main__":
    try:
        fix_users_table()
    except Exception as e:
        print(f"\n[FAIL] Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()

