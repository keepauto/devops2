"""empty message

Revision ID: 4f8d706072a1
Revises: 2236c975e81e
Create Date: 2016-05-29 18:08:02.127376

"""

# revision identifiers, used by Alembic.
revision = '4f8d706072a1'
down_revision = '2236c975e81e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cabinet', sa.Column('power', sa.Integer(), nullable=True))
    op.drop_column('cabinet', 'ower')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cabinet', sa.Column('ower', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('cabinet', 'power')
    ### end Alembic commands ###
