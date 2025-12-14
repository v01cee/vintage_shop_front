"""
API endpoints для пользователей с JWT аутентификацией и БД
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import User
from app.schemas.user import User as UserSchema, UserCreate, UserUpdate, UserLogin
from typing import Optional
from app.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from app.exceptions import NotFoundError, ValidationError, ConflictError, UnauthorizedError, DatabaseError
from app.validators import validate_phone_or_email, validate_password
from datetime import timedelta
from typing import Optional

router = APIRouter()


@router.post("/users/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def register_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    """
    Регистрация нового пользователя
    
    - **phone_or_email**: Телефон или email (валидируется)
    - **password**: Пароль (минимум 6 символов)
    - **full_name**: ФИО (опционально)
    - **phone**: Телефон для доставки (опционально)
    - **address**: Адрес доставки (опционально)
    
    Rate limit: 10 регистраций в час с одного IP
    """
    # Rate limiting применяется через декоратор в main.py
    # Валидация
    validate_phone_or_email(user.phone_or_email)
    validate_password(user.password)
    
    # Логируем попытку регистрации
    print(f"[DEBUG] Попытка регистрации: phone_or_email={user.phone_or_email}")
    
    # Проверяем, существует ли пользователь
    # Используем fresh query без кэша
    db.expire_all()  # Очищаем кэш сессии
    existing_user = db.query(User).filter(
        User.phone_or_email == user.phone_or_email
    ).first()
    
    if existing_user:
        # Логируем для отладки
        print(f"[DEBUG] Найден существующий пользователь: ID={existing_user.id}, phone_or_email={existing_user.phone_or_email}")
        print(f"[DEBUG] Тип: {type(existing_user)}, Значение: {existing_user.phone_or_email}")
        raise ConflictError("Пользователь с таким телефоном/email уже существует")
    
    print(f"[DEBUG] Пользователь не найден, создаем нового: phone_or_email={user.phone_or_email}")
    
    # Защита от установки роли admin через регистрацию
    from app.models import UserRole
    user_role = user.role if user.role and user.role == UserRole.BUYER else UserRole.BUYER
    
    # Создаем нового пользователя
    try:
        new_user = User(
            phone_or_email=user.phone_or_email,
            password_hash=get_password_hash(user.password),
            full_name=user.full_name,
            phone=user.phone,
            address=user.address,
            role=user_role  # Всегда buyer при регистрации
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as e:
        db.rollback()
        print(f"[DEBUG] IntegrityError при создании пользователя: {str(e)}")
        # Проверяем, что именно вызвало ошибку
        if "phone_or_email" in str(e).lower() or "unique" in str(e).lower():
            raise ConflictError("Пользователь с таким телефоном/email уже существует")
        else:
            raise DatabaseError(f"Ошибка целостности данных: {str(e)}")
    except Exception as e:
        db.rollback()
        # Логируем полную ошибку для отладки
        import traceback
        error_details = traceback.format_exc()
        print(f"Ошибка при создании пользователя: {str(e)}")
        print(f"Traceback: {error_details}")
        raise DatabaseError(f"Ошибка при создании пользователя: {str(e)}")


@router.post("/users/login")
async def login_user(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    credentials: Optional[UserLogin] = None,
    db: Session = Depends(get_db)
):
    """
    Вход пользователя
    
    Возвращает JWT токен и данные пользователя.
    Токен действителен 30 дней.
    
    Поддерживает два формата:
    - Form data (OAuth2): username=...&password=... (для Swagger UI)
    - JSON: {"phone_or_email": "...", "password": "..."}
    
    Rate limit: 5 попыток в минуту с одного IP
    """
    # Rate limiting применяется через декоратор в main.py
    # Поддержка OAuth2 form data из Swagger UI (приоритет)
    if form_data.username and form_data.password:
        phone_or_email = form_data.username
        pwd = form_data.password
    elif credentials:
        phone_or_email = credentials.phone_or_email
        pwd = credentials.password
    else:
        raise ValidationError("Требуется phone_or_email/username и password")
    
    # Валидация
    validate_phone_or_email(phone_or_email)
    
    # Ищем пользователя
    user = db.query(User).filter(
        User.phone_or_email == phone_or_email
    ).first()
    
    if not user:
        raise UnauthorizedError("Неверный телефон/email или пароль")
    
    # Проверяем пароль
    if not verify_password(pwd, user.password_hash):
        raise UnauthorizedError("Неверный телефон/email или пароль")
    
    # Создаем токен (sub должен быть строкой для JWT)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


@router.get("/users/me", response_model=UserSchema)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    Получить информацию о текущем пользователе
    
    Требует JWT токен в заголовке Authorization: Bearer <token>
    """
    return current_user


@router.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получить пользователя по ID
    
    - **user_id**: ID пользователя
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundError("Пользователь")
    return user


@router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Обновить данные пользователя
    
    Можно обновить только свои данные (проверяется по токену).
    Только админ может менять роли.
    
    - **user_id**: ID пользователя (должен совпадать с текущим пользователем, или быть админом)
    - **full_name**: ФИО (опционально)
    - **phone**: Телефон для доставки (опционально)
    - **address**: Адрес доставки (опционально)
    - **password**: Новый пароль (опционально, валидируется)
    - **role**: Роль (опционально, только для админа)
    """
    from app.models import UserRole
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundError("Пользователь")
    
    # Проверяем права доступа
    is_admin = current_user.role == UserRole.ADMIN
    is_own_profile = current_user.id == user_id
    
    if not (is_admin or is_own_profile):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Можно обновлять только свои данные"
        )
    
    # Обновляем данные
    update_data = user_update.dict(exclude_unset=True)
    
    # Только админ может менять роли
    if "role" in update_data and not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Только администратор может менять роли"
        )
    
    if "password" in update_data:
        validate_password(update_data["password"])
        update_data["password_hash"] = get_password_hash(update_data.pop("password"))
    
    try:
        for field, value in update_data.items():
            setattr(user, field, value)
        
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при обновлении пользователя: {str(e)}")
