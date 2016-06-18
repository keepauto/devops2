"""empty message

Revision ID: 18c55de88a3d
Revises: None
Create Date: 2016-06-03 15:26:28.876799

"""

# revision identifiers, used by Alembic.
revision = '18c55de88a3d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('idc_name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('user_interface', sa.String(length=50), nullable=False),
    sa.Column('user_phone', sa.String(length=50), nullable=False),
    sa.Column('rel_cabinet_num', sa.Integer(), nullable=False),
    sa.Column('pact_cabinet_num', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_idc_name'), 'idc', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_idc_name'), table_name='idc')
    op.drop_table('idc')
    ### end Alembic commands ###