from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.api.v1 import products, cart, users, orders, order_comments, reviews, uploads
from app.exceptions import BaseAPIException
from app.tasks.order_tasks import cancel_unpaid_orders
import logging
import atexit
import os

app = FastAPI(
    title="Vintage Shop API",
    description="API для магазина винтажных товаров",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Настройка Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Применяем rate limiting к endpoints через декораторы
from app.api.v1 import users as users_router
# Декораторы применяются напрямую в роутерах через app.state.limiter

# Настройка CORS для работы с фронтендом
# origins берём из переменной окружения CORS_ORIGINS (через запятую)
raw_cors = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:3000,http://localhost:3001,http://localhost:5173"
)
cors_origins = [origin.strip() for origin in raw_cors.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение статических файлов для загруженных изображений
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Подключение роутеров
app.include_router(products.router, prefix="/api/v1", tags=["products"])
app.include_router(cart.router, prefix="/api/v1", tags=["cart"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(orders.router, prefix="/api/v1", tags=["orders"])
app.include_router(order_comments.router, prefix="/api/v1", tags=["order-comments"])
app.include_router(reviews.router, prefix="/api/v1", tags=["reviews"])
app.include_router(uploads.router, prefix="/api/v1", tags=["uploads"])

# Применяем rate limiting к endpoints после подключения роутеров
# Находим нужные endpoints и применяем декораторы
for route in users.router.routes:
    if hasattr(route, 'path') and route.path == "/users/login":
        route.endpoint = limiter.limit("5/minute")(route.endpoint)
    elif hasattr(route, 'path') and route.path == "/users/register":
        route.endpoint = limiter.limit("10/hour")(route.endpoint)

# Настройка фоновых задач
scheduler = BackgroundScheduler()
scheduler.add_job(
    cancel_unpaid_orders,
    trigger=IntervalTrigger(minutes=1),  # Запуск каждую минуту
    id='cancel_unpaid_orders',
    name='Отмена неоплаченных заказов',
    replace_existing=True
)
scheduler.start()

# Останавливаем scheduler при завершении приложения
atexit.register(lambda: scheduler.shutdown())

# Настройка логирования для фоновых задач
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Фоновая задача для отмены неоплаченных заказов запущена (проверка каждую минуту)")


@app.get("/")
async def root():
    return {"message": "Vintage Shop API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# Обработчики ошибок
@app.exception_handler(BaseAPIException)
async def api_exception_handler(request: Request, exc: BaseAPIException):
    """Обработка кастомных исключений API"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Обработка ошибок валидации Pydantic"""
    # Конвертируем ошибки в сериализуемый формат
    errors = []
    for error in exc.errors():
        error_dict = error.copy()
        # Конвертируем bytes в строку, если есть
        if 'input' in error_dict and isinstance(error_dict['input'], bytes):
            error_dict['input'] = error_dict['input'].decode('utf-8', errors='replace')
        errors.append(error_dict)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": errors}
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """Обработка ошибок SQLAlchemy"""
    logging.exception("Database error")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Ошибка базы данных"}
    )
