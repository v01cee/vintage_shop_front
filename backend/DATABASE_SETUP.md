# Настройка базы данных

## Шаг 1: Создать файл .env

Создайте файл `.env` в папке `backend/` со следующим содержимым:

```env
# URL подключения к базе данных
# Формат: postgresql://user:password@host:port/database
DATABASE_URL=postgresql://user:password@localhost:5432/vintage_shop

# CORS origins (разделенные запятыми)
CORS_ORIGINS=http://localhost:3000,http://localhost:3001,http://localhost:5173
```

**Замените значения на ваши реальные данные БД:**
- `user` - имя пользователя БД
- `password` - пароль БД
- `localhost:5432` - хост и порт БД
- `vintage_shop` - название базы данных

## Шаг 2: Создать базу данных

Если используете PostgreSQL:

```sql
CREATE DATABASE vintage_shop;
```

Или через psql:
```bash
psql -U postgres
CREATE DATABASE vintage_shop;
```

## Шаг 3: Создать миграции

```bash
cd backend
alembic revision --autogenerate -m "Initial migration"
```

## Шаг 4: Применить миграции

```bash
alembic upgrade head
```

Это создаст все таблицы в базе данных.

## Шаг 5: Проверить подключение

Запустите сервер:
```bash
uvicorn main:app --reload
```

Если всё настроено правильно, сервер запустится без ошибок.

---

## Поддержка других БД

### MySQL:
```env
DATABASE_URL=mysql://user:password@localhost:3306/vintage_shop
```

### SQLite (для разработки):
```env
DATABASE_URL=sqlite:///./vintage_shop.db
```

---

## Полезные команды Alembic

- `alembic current` - показать текущую версию миграции
- `alembic history` - показать историю миграций
- `alembic upgrade head` - применить все миграции
- `alembic downgrade -1` - откатить последнюю миграцию
- `alembic revision --autogenerate -m "описание"` - создать новую миграцию
