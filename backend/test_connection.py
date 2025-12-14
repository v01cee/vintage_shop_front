#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для проверки подключения к БД
"""
from app.database import engine

try:
    with engine.connect() as conn:
        print("✅ Подключение к БД успешно!")
        print(f"База данных: {engine.url.database}")
        print(f"Хост: {engine.url.host}")
except Exception as e:
    print(f"❌ Ошибка подключения к БД: {e}")
    exit(1)

