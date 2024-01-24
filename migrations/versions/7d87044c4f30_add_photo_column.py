"""add photo column

Revision ID: 7d87044c4f30
Revises: 4b2c6330a77c
Create Date: 2024-01-24 07:46:20.369232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d87044c4f30'
down_revision = '4b2c6330a77c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('photo')

    # ### end Alembic commands ###