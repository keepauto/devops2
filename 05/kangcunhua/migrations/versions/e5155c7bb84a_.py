"""empty message

Revision ID: e5155c7bb84a
Revises: df4e333b7863
Create Date: 2016-06-20 17:06:43.712683

"""

# revision identifiers, used by Alembic.
revision = 'e5155c7bb84a'
down_revision = 'df4e333b7863'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server', 'ipinfo')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('ipinfo', mysql.VARCHAR(length=50), nullable=True))
    ### end Alembic commands ###