#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Проверка индексов на таблице users
"""
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
engine = create_engine(DATABASE_URL)

def check_indexes():
    """Проверка индексов"""
    print("=" * 60)
    print("Проверка индексов на таблице users")
    print("=" * 60)
    
    with engine.connect() as conn:
        # Получаем все индексы
        result = conn.execute(text("""
            SELECT 
                indexname, 
                indexdef 
            FROM pg_indexes 
            WHERE tablename = 'users';
        """))
        
        indexes = result.fetchall()
        print(f"\nВсего индексов: {len(indexes)}")
        for idx in indexes:
            print(f"\n  Имя: {idx[0]}")
            print(f"  Определение: {idx[1]}")
        
        # Проверяем уникальный индекс на phone_or_email
        print("\n" + "=" * 60)
        print("Проверка уникального индекса на phone_or_email")
        print("=" * 60)
        
        # Пытаемся создать тестовую запись
        try:
            conn.execute(text("""
                INSERT INTO users (phone_or_email, password_hash, full_name)
                VALUES ('test@example.com', 'test_hash', 'Test User');
            """))
            conn.commit()
            print("[OK] Тестовая запись создана успешно")
            
            # Пытаемся создать дубликат
            try:
                conn.execute(text("""
                    INSERT INTO users (phone_or_email, password_hash, full_name)
                    VALUES ('test@example.com', 'test_hash2', 'Test User 2');
                """))
                conn.commit()
                print("[FAIL] Дубликат был создан - уникальный индекс не работает!")
            except Exception as e:
                print(f"[OK] Дубликат не создан (как и должно быть): {str(e)[:100]}")
            
            # Удаляем тестовую запись
            conn.execute(text("DELETE FROM users WHERE phone_or_email = 'test@example.com';"))
            conn.commit()
            print("[OK] Тестовая запись удалена")
            
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Ошибка при тестировании: {e}")

if __name__ == "__main__":
    check_indexes()



