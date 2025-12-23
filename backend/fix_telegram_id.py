#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Исправление колонки telegram_id - делаем её nullable
"""
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
engine = create_engine(DATABASE_URL)

def fix_telegram_id():
    """Делаем telegram_id nullable"""
    print("=" * 60)
    print("Исправление колонки telegram_id")
    print("=" * 60)
    
    with engine.connect() as conn:
        try:
            # Проверяем текущее состояние
            result = conn.execute(text("""
                SELECT column_name, is_nullable, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'users' AND column_name = 'telegram_id';
            """))
            col_info = result.fetchone()
            
            if col_info:
                print(f"\nТекущее состояние telegram_id:")
                print(f"  is_nullable: {col_info[1]}")
                print(f"  data_type: {col_info[2]}")
                
                if col_info[1] == 'NO':
                    print("\nДелаем telegram_id nullable...")
                    conn.execute(text("ALTER TABLE users ALTER COLUMN telegram_id DROP NOT NULL;"))
                    conn.commit()
                    print("[OK] Колонка telegram_id теперь nullable")
                else:
                    print("\n[OK] Колонка telegram_id уже nullable")
            else:
                print("\n[WARN] Колонка telegram_id не найдена")
                
        except Exception as e:
            conn.rollback()
            print(f"\n[FAIL] Ошибка: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    fix_telegram_id()



