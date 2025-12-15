"""
API endpoints для загрузки изображений
"""
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from typing import List
from app.auth import get_current_user, get_current_admin
from app.models import User
from app.utils.file_upload import (
    save_uploaded_file,
    save_multiple_files,
    PRODUCTS_UPLOAD_DIR,
    REVIEWS_UPLOAD_DIR,
    delete_file
)

router = APIRouter()


@router.post("/uploads/products", status_code=status.HTTP_201_CREATED)
async def upload_product_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_admin)
):
    """
    Загрузить изображение для товара
    
    Требует права администратора.
    
    - **file**: Изображение (jpg, jpeg, png, gif, webp)
    - Изображение автоматически оптимизируется
    
    Returns:
        - **url**: URL загруженного изображения
    """
    try:
        url = await save_uploaded_file(file, PRODUCTS_UPLOAD_DIR)
        return {"url": url, "message": "Изображение успешно загружено"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при загрузке файла: {str(e)}"
        )


@router.post("/uploads/products/multiple", status_code=status.HTTP_201_CREATED)
async def upload_product_images(
    files: List[UploadFile] = File(...),
    current_user: User = Depends(get_current_admin)
):
    """
    Загрузить несколько изображений для товара
    
    Требует права администратора.
    
    - **files**: Список изображений (максимум 10)
    
    Returns:
        - **urls**: Список URL загруженных изображений
    """
    try:
        urls = await save_multiple_files(files, PRODUCTS_UPLOAD_DIR, max_files=10)
        return {"urls": urls, "count": len(urls), "message": "Изображения успешно загружены"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при загрузке файлов: {str(e)}"
        )


@router.post("/uploads/reviews", status_code=status.HTTP_201_CREATED)
async def upload_review_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    Загрузить изображение для отзыва
    
    Требует JWT токен.
    
    - **file**: Изображение (jpg, jpeg, png, gif, webp)
    - Изображение автоматически оптимизируется
    
    Returns:
        - **url**: URL загруженного изображения
    """
    try:
        url = await save_uploaded_file(file, REVIEWS_UPLOAD_DIR)
        return {"url": url, "message": "Изображение успешно загружено"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при загрузке файла: {str(e)}"
        )


@router.post("/uploads/reviews/multiple", status_code=status.HTTP_201_CREATED)
async def upload_review_images(
    files: List[UploadFile] = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    Загрузить несколько изображений для отзыва
    
    Требует JWT токен.
    
    - **files**: Список изображений (максимум 5)
    
    Returns:
        - **urls**: Список URL загруженных изображений
    """
    try:
        urls = await save_multiple_files(files, REVIEWS_UPLOAD_DIR, max_files=5)
        return {"urls": urls, "count": len(urls), "message": "Изображения успешно загружены"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при загрузке файлов: {str(e)}"
        )


@router.delete("/uploads/{file_path:path}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_uploaded_file(
    file_path: str,
    current_user: User = Depends(get_current_admin)
):
    """
    Удалить загруженный файл
    
    Требует права администратора.
    
    - **file_path**: Путь к файлу (например, "products/abc123.jpg")
    """
    # Проверяем, что путь безопасный (не содержит ..)
    if ".." in file_path or file_path.startswith("/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Недопустимый путь к файлу"
        )
    
    full_path = f"/uploads/{file_path}"
    if delete_file(full_path):
        return None
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Файл не найден"
        )
