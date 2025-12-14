from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models import UserRole


class UserBase(BaseModel):
    phone_or_email: str
    full_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class UserCreate(UserBase):
    password: str
    role: Optional[UserRole] = UserRole.BUYER  # По умолчанию покупатель


class UserUpdate(BaseModel):
    phone_or_email: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[UserRole] = None  # Только админ может менять роли


class UserLogin(BaseModel):
    phone_or_email: str
    password: str


class User(UserBase):
    id: int
    role: UserRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
