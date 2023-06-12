"""add password_hash

Revision ID: 2e5d4f5c8f01
Revises: 8e0cd56aecc4
Create Date: 2023-06-04 20:03:02.644260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e5d4f5c8f01'
down_revision = '8e0cd56aecc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=False))
        batch_op.drop_column('login')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('login', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
