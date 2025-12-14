from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ReviewBase(BaseModel):
    text: str
    images: Optional[List[str]] = None


class ReviewCreate(ReviewBase):
    product_id: int


class ReviewUpdate(BaseModel):
    text: Optional[str] = None
    images: Optional[List[str]] = None
    seller_response: Optional[str] = None


class Review(ReviewBase):
    id: int
    user_id: int
    product_id: int
    seller_response: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
