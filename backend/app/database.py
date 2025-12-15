import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строку подключения берём из переменных окружения
# В продакшене ОБЯЗАТЕЛЬНО задать DATABASE_URL
# Для локальной разработки по умолчанию используем SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

# Создаем движок SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Проверка соединения перед использованием
    echo=False  # Установить True для отладки SQL запросов
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()


def get_db():
    """Dependency для получения сессии БД.
    Используется в FastAPI endpoints через Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
