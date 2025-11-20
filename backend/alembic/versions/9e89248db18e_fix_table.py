"""Fix table

Revision ID: 9e89248db18e
Revises: 62a3404cba86
Create Date: 2025-11-19 20:07:25.325781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e89248db18e'
down_revision: Union[str, Sequence[str], None] = '62a3404cba86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('tasks', 'created_at',
                    server_default=sa.text('CURRENT_TIMESTAMP'),
                    existing_type=sa.DateTime(),
                    existing_nullable=False)

def downgrade():
    op.alter_column('tasks', 'created_at',
                    server_default=None,
                    existing_type=sa.DateTime(),
                    existing_nullable=False)