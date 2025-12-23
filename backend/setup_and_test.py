#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для установки зависимостей и запуска тестов
"""
import subprocess
import sys
import os

def run_command(cmd, description):
    """Выполнение команды"""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def main():
    print("="*60)
    print("Установка зависимостей и запуск тестов")
    print("="*60)
    
    # Шаг 1: Установка зависимостей
    if not run_command("pip install -r requirements.txt", "Установка зависимостей..."):
        print("\n[ОШИБКА] Не удалось установить зависимости")
        print("Попробуйте вручную: pip install -r requirements.txt")
        return
    
    # Шаг 2: Проверка подключения к БД
    print("\n" + "="*60)
    print("Проверка подключения к БД...")
    print("="*60)
    try:
        from app.database import engine
        with engine.connect() as conn:
            print("[OK] Подключение к БД успешно!")
    except Exception as e:
        print(f"[ОШИБКА] Ошибка подключения к БД: {e}")
        print("Проверьте файл .env и настройки DATABASE_URL")
        return
    
    # Шаг 3: Запуск тестов
    print("\n" + "="*60)
    print("Запуск тестов...")
    print("="*60)
    run_command("pytest tests/ -v", "Выполнение тестов pytest...")
    
    print("\n" + "="*60)
    print("Готово!")
    print("="*60)
    print("\nДля запуска сервера выполните:")
    print("uvicorn main:app --reload --port 8000")
    print("\nЗатем откройте в браузере:")
    print("http://localhost:8000/docs")

if __name__ == "__main__":
    main()



