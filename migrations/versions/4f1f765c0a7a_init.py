"""init

Revision ID: 4f1f765c0a7a
Revises: 9edb54dbe549
Create Date: 2022-06-17 10:24:18.817504

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '4f1f765c0a7a'
down_revision = '9edb54dbe549'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###