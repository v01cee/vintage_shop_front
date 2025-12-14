# Инструкция по тестированию API

## Быстрый старт

### 1. Установите зависимости

```bash
cd backend
pip install -r requirements.txt
```

### 2. Проверьте установку

```bash
python check_setup.py
```

Этот скрипт проверит:
- Установлены ли все зависимости
- Подключение к базе данных

### 3. Запустите тесты

```bash
pytest tests/ -v
```

Или запустите все сразу:
```bash
python setup_and_test.py
```

## Запуск сервера для ручного тестирования

### 1. Запустите сервер

```bash
uvicorn main:app --reload --port 8000
```

### 2. Откройте Swagger UI

Откройте в браузере: http://localhost:8000/docs

### 3. Протестируйте endpoints

В Swagger UI вы можете:
- Просмотреть все доступные endpoints
- Протестировать их интерактивно
- Увидеть примеры запросов и ответов

### 4. Автоматическое тестирование (опционально)

В другом терминале (после запуска сервера):
```bash
python test_api.py
```

## Ожидаемые результаты

### Тесты должны пройти:
- ✅ test_users.py - 10+ тестов
- ✅ test_products.py - 8+ тестов  
- ✅ test_cart.py - 6+ тестов

### Основные endpoints для проверки:

1. **Health check**: `GET /health`
2. **Получение товаров**: `GET /api/v1/products`
3. **Регистрация**: `POST /api/v1/users/register`
4. **Вход**: `POST /api/v1/users/login`
5. **Получение текущего пользователя**: `GET /api/v1/users/me` (требует токен)
6. **Корзина**: `GET /api/v1/cart` (требует токен)

## Решение проблем

### Ошибка "ModuleNotFoundError"
Установите зависимости: `pip install -r requirements.txt`

### Ошибка подключения к БД
Проверьте файл `.env` и настройки `DATABASE_URL`

### Ошибка "ARRAY type not supported"
Тесты автоматически конвертируют ARRAY в JSON для SQLite

### Тесты не запускаются
Убедитесь, что установлен pytest: `pip install pytest pytest-asyncio httpx`

