"""
JWT аутентификация
"""
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.exceptions import UnauthorizedError

# Настройки JWT
# Захардкоженный SECRET_KEY
SECRET_KEY = "vintage-shop-secret-key-2025-production-change-if-needed"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60  # 30 дней

# Настройки для хеширования паролей
# Используем bcrypt с явной настройкой
# Подавляем предупреждение о версии bcrypt (не критично для работы)
import warnings
import logging

# Подавляем предупреждения от passlib/bcrypt
logging.getLogger("passlib").setLevel(logging.ERROR)
warnings.filterwarnings("ignore", message=".*bcrypt.*", category=UserWarning)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__rounds=12,
    deprecated="auto"
)

# OAuth2 схема
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверка пароля"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Хеширование пароля"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Создание JWT токена"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    """Проверка и декодирование токена"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Получить текущего пользователя из токена"""
    payload = verify_token(token)
    if payload is None:
        raise UnauthorizedError("Неверный токен")
    
    user_id_str = payload.get("sub")
    if user_id_str is None:
        raise UnauthorizedError("Неверный токен")
    
    # Конвертируем строку обратно в int
    try:
        user_id = int(user_id_str)
    except (ValueError, TypeError):
        raise UnauthorizedError("Неверный формат токена")
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise UnauthorizedError("Пользователь не найден")
    
    return user


async def get_current_user_optional(
    token: Optional[str] = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """Получить текущего пользователя (опционально, для публичных endpoints)"""
    if token is None:
        return None
    
    try:
        return await get_current_user(token, db)
    except:
        return None


async def get_current_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    """Получить текущего пользователя с проверкой прав администратора"""
    from app.models import UserRole
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Требуются права администратора"
        )
    return current_user
