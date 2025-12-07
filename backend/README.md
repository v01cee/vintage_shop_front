# Vintage Shop Backend API

FastAPI бэкенд для торговой площадки винтажных товаров.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload --port 8000
```

API будет доступен по адресу: http://localhost:8000

Документация API: http://localhost:8000/docs

## Структура проекта

```
backend/
├── main.py              # Точка входа приложения
├── requirements.txt     # Зависимости Python
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── products.py  # Эндпоинты для товаров
│   │       └── cart.py      # Эндпоинты для корзины
│   └── schemas/
│       ├── product.py       # Схемы данных для товаров
│       └── cart.py          # Схемы данных для корзины
```

## API Endpoints

### Товары
- `GET /api/v1/products` - Получить список товаров
- `GET /api/v1/products/{product_id}` - Получить товар по ID
- `POST /api/v1/products` - Создать товар
- `PUT /api/v1/products/{product_id}` - Обновить товар
- `DELETE /api/v1/products/{product_id}` - Удалить товар

### Корзина
- `GET /api/v1/cart/{user_id}` - Получить корзину
- `POST /api/v1/cart/{user_id}/items` - Добавить товар в корзину
- `PUT /api/v1/cart/{user_id}/items/{item_id}` - Обновить количество
- `DELETE /api/v1/cart/{user_id}/items/{item_id}` - Удалить товар из корзины
- `DELETE /api/v1/cart/{user_id}` - Очистить корзину

