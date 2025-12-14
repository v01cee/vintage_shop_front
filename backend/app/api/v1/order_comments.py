"""
API endpoints для комментариев к заказам с БД и JWT аутентификацией
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import OrderComment, Order
from app.schemas.order_comment import OrderComment as OrderCommentSchema, OrderCommentCreate
from app.auth import get_current_user, get_current_user_optional
from app.models import User
from app.exceptions import NotFoundError, ValidationError, DatabaseError, ForbiddenError

router = APIRouter()


@router.get("/orders/{order_id}/comments", response_model=List[OrderCommentSchema])
async def get_order_comments(
    order_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Получить комментарии к заказу
    
    Пользователь может просматривать комментарии только к своим заказам.
    
    - **order_id**: ID заказа
    """
    # Проверяем существование заказа
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Проверяем права доступа
    if current_user and order.user_id != current_user.id:
        raise ForbiddenError("Можно просматривать комментарии только к своим заказам")
    
    comments = db.query(OrderComment).filter(
        OrderComment.order_id == order_id
    ).order_by(OrderComment.created_at.asc()).all()
    
    return comments


@router.post("/orders/{order_id}/comments", response_model=OrderCommentSchema, status_code=status.HTTP_201_CREATED)
async def create_order_comment(
    order_id: int,
    comment: OrderCommentCreate,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Создать комментарий к заказу
    
    Пользователь может комментировать только свои заказам.
    Продавец может комментировать любые заказы (is_seller=True).
    
    - **order_id**: ID заказа
    - **text**: Текст комментария (обязательно)
    - **is_seller**: Комментарий от продавца (по умолчанию False)
    """
    # Проверяем существование заказа
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise NotFoundError("Заказ")
    
    # Валидация текста
    if not comment.text or not comment.text.strip():
        raise ValidationError("Текст комментария не может быть пустым")
    
    # Проверяем права доступа
    if comment.is_seller:
        # Продавец может комментировать любые заказы
        user_id = None
    else:
        # Пользователь может комментировать только свои заказы
        if not current_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Требуется аутентификация для создания комментария"
            )
        if order.user_id != current_user.id:
            raise ForbiddenError("Можно комментировать только свои заказы")
        user_id = current_user.id
    
    try:
        new_comment = OrderComment(
            order_id=order_id,
            user_id=user_id,
            is_seller=comment.is_seller,
            text=comment.text.strip()
        )
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при создании комментария: {str(e)}")


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Удалить комментарий
    
    Пользователь может удалить только свои комментарии.
    Продавец может удалить любые комментарии (требуется дополнительная проверка прав).
    
    - **comment_id**: ID комментария
    """
    comment = db.query(OrderComment).filter(OrderComment.id == comment_id).first()
    if not comment:
        raise NotFoundError("Комментарий")
    
    # Проверяем права доступа
    if comment.user_id != current_user.id and not comment.is_seller:
        raise ForbiddenError("Можно удалять только свои комментарии")
    
    try:
        db.delete(comment)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при удалении комментария: {str(e)}")
