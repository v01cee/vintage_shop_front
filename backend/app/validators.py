"""
Валидация данных
"""
import re
from typing import Optional
from app.exceptions import ValidationError

# Регулярные выражения для валидации
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{1,14}$')  # E.164 формат


def validate_email_or_phone(value: str) -> tuple[bool, str]:
    """
    Валидация email или телефона
    Возвращает (is_valid, type) где type: 'email', 'phone' или 'invalid'
    """
    if EMAIL_PATTERN.match(value):
        return True, 'email'
    elif PHONE_PATTERN.match(value):
        return True, 'phone'
    else:
        return False, 'invalid'


def validate_phone_or_email(value: str) -> None:
    """Проверка и выброс исключения если невалидно"""
    is_valid, _ = validate_email_or_phone(value)
    if not is_valid:
        raise ValidationError("Неверный формат email или телефона")


def validate_price(price: float, min_price: float = 0.0) -> None:
    """Валидация цены"""
    if price < min_price:
        raise ValidationError(f"Цена должна быть не менее {min_price}")
    if price > 100000000:  # Максимальная цена
        raise ValidationError("Цена слишком большая")


def validate_quantity(quantity: int, min_quantity: int = 0) -> None:
    """Валидация количества"""
    if quantity < min_quantity:
        raise ValidationError(f"Количество должно быть не менее {min_quantity}")
    if quantity > 10000:  # Максимальное количество
        raise ValidationError("Количество слишком большое")


def validate_order_status(status: str) -> None:
    """Валидация статуса заказа"""
    valid_statuses = ["new", "paid", "in_progress", "sent", "cancelled", "return"]
    if status not in valid_statuses:
        raise ValidationError(f"Неверный статус заказа. Допустимые: {', '.join(valid_statuses)}")


def validate_password(password: str) -> None:
    """Валидация пароля"""
    if len(password) < 6:
        raise ValidationError("Пароль должен содержать минимум 6 символов")
    if len(password) > 100:
        raise ValidationError("Пароль слишком длинный")
