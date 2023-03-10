"""add tags

Revision ID: 818a5bfb10f0
Revises: 41b1fe67d9ff
Create Date: 2023-03-07 16:46:35.027262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '818a5bfb10f0'
down_revision = '41b1fe67d9ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
