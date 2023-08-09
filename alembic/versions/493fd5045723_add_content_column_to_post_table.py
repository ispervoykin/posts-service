"""add content column to post table

Revision ID: 493fd5045723
Revises: ebc02b86e9f8
Create Date: 2023-08-08 19:25:38.452812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '493fd5045723'
down_revision: Union[str, None] = 'ebc02b86e9f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
