#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для очистки старых записей с NULL в phone_or_email
"""
from sqlalchemy import create_engine, text

# Захардкоженный DATABASE_URL (временно)
DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"

engine = create_engine(DATABASE_URL)

def cleanup_null_users():
    """Удаление записей с NULL в phone_or_email"""
    print("=" * 60)
    print("Очистка старых записей с NULL в phone_or_email")
    print("=" * 60)
    
    with engine.connect() as conn:
        # Сначала проверяем количество
        result = conn.execute(text("SELECT COUNT(*) FROM users WHERE phone_or_email IS NULL;"))
        null_count = result.scalar()
        
        print(f"\nНайдено записей с NULL в phone_or_email: {null_count}")
        
        if null_count == 0:
            print("\n[OK] Нет записей для удаления")
            return
        
        # Показываем, что будет удалено
        print("\nЗаписи, которые будут удалены:")
        result = conn.execute(text("""
            SELECT id, full_name, created_at 
            FROM users 
            WHERE phone_or_email IS NULL
            ORDER BY id;
        """))
        
        rows = result.fetchall()
        for row in rows:
            print(f"  ID: {row[0]}, full_name: {row[1]}, created_at: {row[2]}")
        
        # Спрашиваем подтверждение (в скрипте просто удаляем)
        print(f"\nУдаляем {null_count} записей...")
        
        try:
            # Удаляем записи с NULL (используем autocommit)
            result = conn.execute(text("DELETE FROM users WHERE phone_or_email IS NULL;"))
            deleted_count = result.rowcount
            conn.commit()
            
            print(f"[OK] Удалено {deleted_count} записей")
            print("\n" + "=" * 60)
            print("[OK] Очистка завершена!")
            print("=" * 60)
            
        except Exception as e:
            conn.rollback()
            print(f"\n[FAIL] Ошибка при удалении: {e}")
            raise

if __name__ == "__main__":
    try:
        cleanup_null_users()
    except Exception as e:
        print(f"\n[FAIL] Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()



