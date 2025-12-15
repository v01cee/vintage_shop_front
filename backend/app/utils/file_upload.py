"""
Утилиты для загрузки и обработки файлов
"""
import os
import uuid
from pathlib import Path
from typing import List, Optional
from fastapi import UploadFile, HTTPException, status
from PIL import Image
import shutil

# Настройки
UPLOAD_DIR = Path("uploads")
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
ALLOWED_IMAGE_MIME_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/gif",
    "image/webp"
}

# Создаем директории для хранения файлов
PRODUCTS_UPLOAD_DIR = UPLOAD_DIR / "products"
REVIEWS_UPLOAD_DIR = UPLOAD_DIR / "reviews"

# Создаем директории, если их нет
PRODUCTS_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REVIEWS_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def validate_image_file(file: UploadFile) -> None:
    """
    Валидация загружаемого изображения
    
    Проверяет:
    - MIME тип
    - Расширение файла
    """
    # Проверка MIME типа
    if file.content_type not in ALLOWED_IMAGE_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неподдерживаемый тип файла. Разрешены: {', '.join(ALLOWED_IMAGE_EXTENSIONS)}"
        )
    
    # Проверка расширения
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неподдерживаемое расширение файла. Разрешены: {', '.join(ALLOWED_IMAGE_EXTENSIONS)}"
        )


async def save_uploaded_file(
    file: UploadFile,
    upload_dir: Path
) -> str:
    """
    Сохраняет загруженный файл и возвращает относительный URL
    
    Args:
        file: Загруженный файл
        upload_dir: Директория для сохранения
    
    Returns:
        str: Относительный URL файла (например, "/uploads/products/abc123.jpg")
    """
    # Валидация
    validate_image_file(file)
    
    # Читаем содержимое файла
    file_content = await file.read()
    
    # Генерируем уникальное имя файла
    file_ext = Path(file.filename).suffix.lower()
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = upload_dir / unique_filename
    
    # Сохраняем файл
    with open(file_path, "wb") as buffer:
        buffer.write(file_content)
    
    # Опционально: оптимизируем изображение
    try:
        optimize_image(file_path)
    except Exception as e:
        # Если не удалось оптимизировать, продолжаем без ошибки
        pass
    
    # Возвращаем относительный URL
    relative_path = file_path.relative_to(Path("."))
    return f"/{relative_path.as_posix()}"


def optimize_image(image_path: Path, max_size: tuple = (1920, 1920), quality: int = 85) -> None:
    """
    Оптимизирует изображение: уменьшает размер и сжимает
    
    Args:
        image_path: Путь к изображению
        max_size: Максимальный размер (ширина, высота)
        quality: Качество JPEG (1-100)
    """
    try:
        with Image.open(image_path) as img:
            # Конвертируем RGBA в RGB для JPEG
            if img.mode in ("RGBA", "P"):
                background = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                img = background
            elif img.mode != "RGB":
                img = img.convert("RGB")
            
            # Изменяем размер, если нужно
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Сохраняем с оптимизацией
            img.save(image_path, "JPEG", quality=quality, optimize=True)
    except Exception:
        # Если не удалось оптимизировать, оставляем оригинал
        pass


async def save_multiple_files(
    files: List[UploadFile],
    upload_dir: Path,
    max_files: int = 10
) -> List[str]:
    """
    Сохраняет несколько файлов и возвращает список URL
    
    Args:
        files: Список загруженных файлов
        upload_dir: Директория для сохранения
        max_files: Максимальное количество файлов
    
    Returns:
        List[str]: Список относительных URL файлов
    """
    if len(files) > max_files:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Слишком много файлов. Максимум: {max_files}"
        )
    
    urls = []
    for file in files:
        url = await save_uploaded_file(file, upload_dir)
        urls.append(url)
    
    return urls


def delete_file(file_url: str) -> bool:
    """
    Удаляет файл по его URL
    
    Args:
        file_url: URL файла (например, "/uploads/products/abc123.jpg")
    
    Returns:
        bool: True если файл удален, False если не найден
    """
    try:
        # Убираем начальный слэш для создания пути
        file_path = Path(file_url.lstrip("/"))
        if file_path.exists():
            file_path.unlink()
            return True
        return False
    except Exception:
        return False


def delete_multiple_files(file_urls: List[str]) -> int:
    """
    Удаляет несколько файлов
    
    Args:
        file_urls: Список URL файлов
    
    Returns:
        int: Количество удаленных файлов
    """
    deleted = 0
    for url in file_urls:
        if delete_file(url):
            deleted += 1
    return deleted
