"""
Конфигурация для тестов
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event, TypeDecorator, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import json

from app.database import Base, get_db
from main import app

# TypeDecorator для конвертации ARRAY в JSON для SQLite
class JSONArray(TypeDecorator):
    """Тип для хранения массива строк как JSON в SQLite"""
    impl = String
    cache_ok = True
    
    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)
        return value
    
    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value)
        return value


# Тестовая БД в памяти (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Включаем поддержку внешних ключей в SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Включаем поддержку внешних ключей в SQLite"""
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Патчим модели для SQLite: заменяем ARRAY на JSONArray
def patch_models_for_sqlite():
    """Заменяет ARRAY на JSONArray в моделях для работы с SQLite"""
    from app import models
    from sqlalchemy import inspect
    
    # Получаем все таблицы из Base.metadata
    for table_name, table in Base.metadata.tables.items():
        for column in table.columns:
            # Если тип - ARRAY, заменяем на JSONArray
            if hasattr(column.type, 'item_type'):
                column.type = JSONArray()


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    """Настройка тестовой БД перед каждым тестом"""
    # Патчим модели для SQLite
    patch_models_for_sqlite()
    
    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    yield
    
    # Удаляем таблицы
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db():
    """Создание тестовой БД для каждого теста"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(db):
    """Создание тестового клиента"""
    def override_get_db():
        try:
            yield db
        finally:
            pass  # Не закрываем, так как это управляется фикстурой db
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(db):
    """Создание тестового пользователя (buyer)"""
    from app.auth import get_password_hash
    from app.models import User, UserRole
    user = User(
        phone_or_email="test@example.com",
        password_hash=get_password_hash("password123"),
        full_name="Test User",
        role=UserRole.BUYER
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def test_admin(db):
    """Создание тестового администратора"""
    from app.auth import get_password_hash
    from app.models import User, UserRole
    admin = User(
        phone_or_email="admin@example.com",
        password_hash=get_password_hash("password123"),
        full_name="Admin User",
        role=UserRole.ADMIN
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


@pytest.fixture
def admin_headers(client, test_admin):
    """Получение заголовков с токеном для администратора"""
    # Используем form data для OAuth2PasswordRequestForm
    response = client.post(
        "/api/v1/users/login",
        data={
            "username": "admin@example.com",
            "password": "password123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    if response.status_code != 200:
        pytest.fail(f"Не удалось авторизоваться как админ: {response.text}")
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def test_product(db):
    """Создание тестового товара"""
    from app.models import Product
    product = Product(
        name="Test Product",
        description="Test Description",
        price=1000.0,
        quantity=10,
        is_available=True,
        images=None,
        tags=None
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@pytest.fixture
def auth_headers(client, test_user):
    """Получение заголовков с токеном для авторизованного пользователя"""
    # Используем form data для OAuth2PasswordRequestForm
    response = client.post(
        "/api/v1/users/login",
        data={
            "username": "test@example.com",  # OAuth2 использует username вместо phone_or_email
            "password": "password123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    # Проверяем ответ и выводим ошибку, если что-то не так
    if response.status_code != 200:
        print(f"Login failed with status {response.status_code}: {response.text}")
        pytest.fail(f"Не удалось войти: {response.status_code} - {response.text}")
    
    data = response.json()
    token = data.get("access_token")
    if not token:
        print(f"Login response: {data}")
        pytest.fail(f"Токен не получен в ответе: {data}")
    
    return {"Authorization": f"Bearer {token}"}
