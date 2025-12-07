from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import products, cart

app = FastAPI(
    title="Vintage Shop API",
    description="API для торговой площадки винтажных товаров",
    version="1.0.0"
)

# Настройка CORS для работы с фронтендом
import os
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001,http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(products.router, prefix="/api/v1", tags=["products"])
app.include_router(cart.router, prefix="/api/v1", tags=["cart"])


@app.get("/")
async def root():
    return {"message": "Vintage Shop API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}

