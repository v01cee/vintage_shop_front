"""
Кастомные исключения для API
"""
from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    """Базовое исключение для API"""
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class NotFoundError(BaseAPIException):
    """Ресурс не найден"""
    def __init__(self, resource: str = "Ресурс"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} не найден"
        )


class ValidationError(BaseAPIException):
    """Ошибка валидации данных"""
    def __init__(self, detail: str = "Ошибка валидации данных"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )


class UnauthorizedError(BaseAPIException):
    """Ошибка аутентификации"""
    def __init__(self, detail: str = "Требуется аутентификация"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )


class ForbiddenError(BaseAPIException):
    """Ошибка доступа"""
    def __init__(self, detail: str = "Доступ запрещен"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )


class ConflictError(BaseAPIException):
    """Конфликт данных (например, дубликат)"""
    def __init__(self, detail: str = "Конфликт данных"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )


class DatabaseError(BaseAPIException):
    """Ошибка базы данных"""
    def __init__(self, detail: str = "Ошибка базы данных"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail
        )
