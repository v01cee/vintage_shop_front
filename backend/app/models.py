from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, ARRAY, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base


class UserRole(str, enum.Enum):
    """Роли пользователей"""
    ADMIN = "admin"
    BUYER = "buyer"


class User(Base):
    """Модель пользователя"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_or_email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(Text, nullable=True)
    role = Column(Enum(UserRole), default=UserRole.BUYER, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связи
    orders = relationship("Order", back_populates="user")
    cart_items = relationship("CartItem", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Product(Base):
    """Модель товара"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)  # Цена от поставщика
    boutique_price = Column(Float, nullable=True)  # Цена в бутиках
    article = Column(String(100), nullable=True, index=True)  # Артикул
    quantity = Column(Integer, default=1)  # Количество на складе
    views = Column(Integer, default=0)  # Количество просмотров
    category = Column(String(100), nullable=True, index=True)
    image = Column(String(500), nullable=True)  # Главное изображение (URL)
    images = Column(ARRAY(String), nullable=True)  # Дополнительные изображения
    tags = Column(ARRAY(String), nullable=True)  # Теги/характеристики
    is_available = Column(Boolean, default=True)  # Доступен ли товар
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связи
    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")
    reviews = relationship("Review", back_populates="product")


class CartItem(Base):
    """Модель товара в корзине"""
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связи
    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")


class Order(Base):
    """Модель заказа"""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    status = Column(String(50), default="new", index=True)  # new, paid, in_progress, sent, cancelled, return
    total_amount = Column(Float, nullable=False)
    delivery_price = Column(Float, default=0.0)
    delivery_address = Column(Text, nullable=False)
    delivery_service = Column(String(100), default="Почта РФ")
    tracking_number = Column(String(100), nullable=True)
    reserved_until = Column(DateTime(timezone=True), nullable=True)  # Резерв на 30 минут
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связи
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    comments = relationship("OrderComment", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    """Модель товара в заказе"""
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # Цена на момент заказа
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Связи
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


class OrderComment(Base):
    """Модель комментария к заказу"""
    __tablename__ = "order_comments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Если от пользователя
    is_seller = Column(Boolean, default=False)  # Комментарий от продавца
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Связи
    order = relationship("Order", back_populates="comments")
    user = relationship("User")


class Review(Base):
    """Модель отзыва"""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    text = Column(Text, nullable=False)
    images = Column(ARRAY(String), nullable=True)  # Изображения в отзыве
    seller_response = Column(Text, nullable=True)  # Ответ продавца
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связи
    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")
