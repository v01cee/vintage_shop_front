# Инструкция по восстановлению переменных окружения

## Что было сделано

Временно захардкожены переменные окружения для отладки проблем с .env файлом.

## Файлы, которые нужно вернуть обратно

### 1. `app/database.py`

**Было (захардкожено):**
```python
# TODO: ВРЕМЕННО ЗАХАРДКОЖЕНО - вернуть обратно к os.getenv()
DATABASE_URL = "postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres"
```

**Вернуть на:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/vintage_shop"
)
```

### 2. `app/auth.py`

**Было (захардкожено):**
```python
# TODO: ВРЕМЕННО ЗАХАРДКОЖЕНО - вернуть обратно к os.getenv()
SECRET_KEY = "your-secret-key-here-change-in-production"
```

**Вернуть на:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
```

### 3. `main.py`

**Было (захардкожено):**
```python
# TODO: ВРЕМЕННО ЗАХАРДКОЖЕНО - вернуть обратно к os.getenv()
cors_origins = "http://localhost:3000,http://localhost:3001,http://localhost:5173,https://109.73.202.83".split(",")
```

**Вернуть на:**
```python
import os
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001,http://localhost:5173").split(",")
```

## Текущие захардкоженные значения

- **DATABASE_URL**: `postgresql://admin:123b1h23b1kgasfbasfas123@109.73.202.83:5435/testing_postgres`
- **SECRET_KEY**: `your-secret-key-here-change-in-production`
- **CORS_ORIGINS**: `http://localhost:3000,http://localhost:3001,http://localhost:5173,https://109.73.202.83`

Эти значения должны быть в файле `.env` в корне папки `backend/`.

## Как вернуть обратно

1. Убедитесь, что файл `.env` существует и содержит все необходимые переменные
2. Найдите все строки с комментарием `# TODO: ВРЕМЕННО ЗАХАРДКОЖЕНО`
3. Замените захардкоженные значения на `os.getenv()` как показано выше
4. Раскомментируйте импорты `os` и `load_dotenv`
5. Удалите этот файл после восстановления



