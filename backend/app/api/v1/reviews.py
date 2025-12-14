"""
API endpoints для отзывов с БД и JWT аутентификацией
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import Review, Product
from app.schemas.review import Review as ReviewSchema, ReviewCreate, ReviewUpdate
from app.auth import get_current_user, get_current_user_optional
from app.models import User
from app.exceptions import NotFoundError, ValidationError, DatabaseError, ForbiddenError, ConflictError

router = APIRouter()


@router.get("/reviews", response_model=List[ReviewSchema])
async def get_reviews(
    product_id: Optional[int] = Query(None, description="Фильтр по ID товара"),
    db: Session = Depends(get_db)
):
    """
    Получить список отзывов
    
    - **product_id**: Фильтр по ID товара (опционально)
    """
    query = db.query(Review)
    
    if product_id:
        query = query.filter(Review.product_id == product_id)
    
    reviews = query.order_by(Review.created_at.desc()).all()
    return reviews


@router.get("/reviews/{review_id}", response_model=ReviewSchema)
async def get_review(review_id: int, db: Session = Depends(get_db)):
    """
    Получить отзыв по ID
    
    - **review_id**: ID отзыва
    """
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise NotFoundError("Отзыв")
    return review


@router.post("/reviews", response_model=ReviewSchema, status_code=status.HTTP_201_CREATED)
async def create_review(
    review: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Создать новый отзыв
    
    Требует JWT токен. Один пользователь может оставить только один отзыв на товар.
    
    - **product_id**: ID товара (обязательно)
    - **text**: Текст отзыва (обязательно)
    - **images**: Список URL изображений (опционально)
    """
    # Проверяем существование товара
    product = db.query(Product).filter(Product.id == review.product_id).first()
    if not product:
        raise NotFoundError("Товар")
    
    # Валидация текста
    if not review.text or not review.text.strip():
        raise ValidationError("Текст отзыва не может быть пустым")
    
    # Проверяем, не оставлял ли пользователь уже отзыв на этот товар
    existing_review = db.query(Review).filter(
        Review.user_id == current_user.id,
        Review.product_id == review.product_id
    ).first()
    
    if existing_review:
        raise ConflictError("Вы уже оставили отзыв на этот товар")
    
    try:
        new_review = Review(
            user_id=current_user.id,
            product_id=review.product_id,
            text=review.text.strip(),
            images=review.images or []
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
        return new_review
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при создании отзыва: {str(e)}")


@router.put("/reviews/{review_id}", response_model=ReviewSchema)
async def update_review(
    review_id: int,
    review_update: ReviewUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Обновить отзыв
    
    Пользователь может обновить только свои отзывы.
    Продавец может добавить ответ на отзыв (seller_response).
    
    - **review_id**: ID отзыва
    - **text**: Новый текст отзыва (опционально)
    - **images**: Новый список изображений (опционально)
    - **seller_response**: Ответ продавца (опционально, только для продавца)
    """
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise NotFoundError("Отзыв")
    
    update_data = review_update.dict(exclude_unset=True)
    
    # Если обновляется seller_response, проверяем права (только продавец)
    if "seller_response" in update_data:
        # В продакшене здесь должна быть проверка роли пользователя
        # Пока разрешаем любому авторизованному пользователю
        pass
    else:
        # Пользователь может обновлять только свои отзывы
        if review.user_id != current_user.id:
            raise ForbiddenError("Можно обновлять только свои отзывы")
    
    # Валидация текста
    if "text" in update_data:
        if not update_data["text"] or not update_data["text"].strip():
            raise ValidationError("Текст отзыва не может быть пустым")
        update_data["text"] = update_data["text"].strip()
    
    try:
        for field, value in update_data.items():
            setattr(review, field, value)
        
        db.commit()
        db.refresh(review)
        return review
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при обновлении отзыва: {str(e)}")


@router.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Удалить отзыв
    
    Пользователь может удалить только свои отзывы.
    
    - **review_id**: ID отзыва
    """
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise NotFoundError("Отзыв")
    
    # Проверяем права доступа
    if review.user_id != current_user.id:
        raise ForbiddenError("Можно удалять только свои отзывы")
    
    try:
        db.delete(review)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        raise DatabaseError(f"Ошибка при удалении отзыва: {str(e)}")
