"""add user table

Revision ID: ff89a82c8391
Revises: 493fd5045723
Create Date: 2023-08-08 19:34:28.359775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff89a82c8391'
down_revision: Union[str, None] = '493fd5045723'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer, nullable=False, primary_key=True), 
                    sa.Column('email', sa.String, nullable=False, unique=True), 
                    sa.Column('password', sa.String, nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
