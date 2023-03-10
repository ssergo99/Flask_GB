"""add relations between tags and articles

Revision ID: 08427e8ab9cc
Revises: 818a5bfb10f0
Create Date: 2023-03-07 16:51:30.976521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08427e8ab9cc'
down_revision = '818a5bfb10f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_association')
    # ### end Alembic commands ###
