from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    delivery_address: str
    delivery_service: str = "Почта РФ"
    delivery_price: float = 0.0


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    tracking_number: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_service: Optional[str] = None


class Order(OrderBase):
    id: int
    order_number: str
    user_id: int
    status: str  # new, paid, in_progress, sent, cancelled, return
    total_amount: float
    tracking_number: Optional[str] = None
    reserved_until: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    items: List[OrderItem] = []

    class Config:
        from_attributes = True
