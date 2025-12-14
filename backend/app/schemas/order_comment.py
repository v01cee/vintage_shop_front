from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderCommentBase(BaseModel):
    text: str


class OrderCommentCreate(OrderCommentBase):
    order_id: int
    is_seller: bool = False


class OrderComment(OrderCommentBase):
    id: int
    order_id: int
    user_id: Optional[int] = None
    is_seller: bool
    created_at: datetime

    class Config:
        from_attributes = True
