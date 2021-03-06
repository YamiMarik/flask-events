"""empty message

Revision ID: bffc535e00d3
Revises: 
Create Date: 2021-12-14 19:03:23.565976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bffc535e00d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('event_name', sa.String(length=64), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=False),
    sa.Column('event_start', sa.DateTime(), nullable=False),
    sa.Column('event_end', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('event_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
