"""Initial Migration

Revision ID: 3591abc4e0ea
Revises:
Create Date: 2023-05-04 20:18:48.125755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3591abc4e0ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('nickname', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('kanban',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('uid', sa.Integer(), nullable=False),
                    sa.Column('type', sa.Integer(), nullable=False),
                    sa.Column('content', sa.Text(), nullable=False),
                    sa.Column('create_time', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kanban')
    op.drop_table('user')
    # ### end Alembic commands ###
