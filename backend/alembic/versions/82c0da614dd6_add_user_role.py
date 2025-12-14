"""add_user_role

Revision ID: 82c0da614dd6
Revises: 0003
Create Date: 2025-12-14

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '82c0da614dd6'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Создаем enum тип для ролей (PostgreSQL)
    op.execute("""
        DO $$ BEGIN
            CREATE TYPE userrole AS ENUM ('admin', 'buyer');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    """)
    
    # Добавляем колонку role в таблицу users
    op.add_column('users', sa.Column('role', sa.Enum('admin', 'buyer', name='userrole'), nullable=True, server_default='buyer'))
    
    # Создаем индекс для role
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    
    # Обновляем существующие записи (если есть) - устанавливаем buyer по умолчанию
    op.execute("UPDATE users SET role = 'buyer' WHERE role IS NULL")


def downgrade() -> None:
    # Удаляем индекс
    op.drop_index(op.f('ix_users_role'), table_name='users')
    
    # Удаляем колонку role
    op.drop_column('users', 'role')
    
    # Удаляем enum тип
    op.execute("DROP TYPE IF EXISTS userrole")
