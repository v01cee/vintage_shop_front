# Инструкция по запуску тестов и проверке API

## Шаг 1: Установка зависимостей

```bash
cd backend
pip install -r requirements.txt
```

Или если используете виртуальное окружение:
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## Шаг 2: Проверка установки

```bash
python check_setup.py
```

Этот скрипт проверит:
- Установлены ли все зависимости
- Подключение к базе данных

## Шаг 3: Запуск тестов

```bash
# Запуск всех тестов
pytest tests/ -v

# Запуск конкретного файла тестов
pytest tests/test_users.py -v

# Запуск с покрытием кода
pytest tests/ --cov=app --cov-report=html
```

## Шаг 4: Запуск сервера для тестирования API

```bash
uvicorn main:app --reload --port 8000
```

Сервер будет доступен на: http://localhost:8000

## Шаг 5: Тестирование через Swagger

1. Откройте браузер: http://localhost:8000/docs
2. Протестируйте endpoints через интерактивный интерфейс

## Шаг 6: Автоматическое тестирование API (опционально)

В другом терминале (после запуска сервера):
```bash
python test_api.py
```

Этот скрипт автоматически протестирует основные endpoints.

## Ожидаемые результаты тестов

- ✅ test_users.py - 10+ тестов (регистрация, вход, обновление)
- ✅ test_products.py - 8+ тестов (CRUD, поиск, валидация)
- ✅ test_cart.py - 6+ тестов (добавление, обновление, удаление)

Все тесты должны пройти успешно.

