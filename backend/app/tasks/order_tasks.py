"""
Фоновые задачи для работы с заказами
"""
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Order
import logging

logger = logging.getLogger(__name__)


def cancel_unpaid_orders():
    """
    Отменяет неоплаченные заказы, у которых истек резерв (30 минут)
    
    Проверяет заказы со статусом "new", у которых reserved_until уже прошло
    и меняет их статус на "cancelled"
    
    Запускается автоматически каждую минуту через APScheduler
    """
    db: Session = SessionLocal()
    try:
        # Получаем текущее время в UTC (совместимо с datetime.utcnow())
        # Используем timezone.utc для совместимости с PostgreSQL timezone-aware полями
        now = datetime.now(timezone.utc)
        
        # Находим заказы со статусом "new", у которых истек резерв
        expired_orders = db.query(Order).filter(
            Order.status == "new",
            Order.reserved_until.isnot(None),
            Order.reserved_until < now
        ).all()
        
        if not expired_orders:
            logger.debug("Нет заказов для отмены")
            return
        
        cancelled_count = 0
        for order in expired_orders:
            order.status = "cancelled"
            cancelled_count += 1
            logger.info(
                f"Заказ {order.order_number} (ID: {order.id}) отменен автоматически "
                f"из-за истечения резерва. Резерв истек: {order.reserved_until}"
            )
        
        db.commit()
        logger.info(f"Автоматически отменено заказов: {cancelled_count}")
        
    except Exception as e:
        db.rollback()
        logger.error(f"Ошибка при отмене неоплаченных заказов: {str(e)}", exc_info=True)
    finally:
        db.close()
