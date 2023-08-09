"""add foreign-key to posts table

Revision ID: a5b753db0e9b
Revises: ff89a82c8391
Create Date: 2023-08-08 20:03:11.317910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5b753db0e9b'
down_revision: Union[str, None] = 'ff89a82c8391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_column('owner_id')
    op.drop_constraint('posts_users_fk', 'posts')
    pass
