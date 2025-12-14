# Быстрый старт с базой данных

## Что уже готово:

✅ Модели SQLAlchemy созданы для всех сущностей  
✅ Настроено подключение к БД через переменные окружения  
✅ Настроен Alembic для миграций  
✅ Добавлены зависимости в requirements.txt

## Что нужно сделать:

### 1. Установить зависимости:
```bash
cd backend
pip install -r requirements.txt
```

### 2. Создать файл `.env` в папке `backend/`:
```env
DATABASE_URL=postgresql://user:password@host:port/database
```

**Замените на ваши реальные данные БД!**

### 3. Создать миграции:
```bash
alembic revision --autogenerate -m "Initial migration"
```

### 4. Применить миграции:
```bash
alembic upgrade head
```

Готово! Таблицы созданы в БД.

---

## Примечание про ARRAY

Модели используют `ARRAY(String)` для полей `images` и `tags`. Это работает только в PostgreSQL.

Если используете MySQL или SQLite, нужно будет изменить на JSON в `app/models.py`:
```python
from sqlalchemy import JSON
# Вместо ARRAY(String) использовать:
images = Column(JSON, nullable=True)
tags = Column(JSON, nullable=True)
```
