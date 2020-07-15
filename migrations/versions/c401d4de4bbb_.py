"""empty message

Revision ID: c401d4de4bbb
Revises: 
Create Date: 2020-07-14 19:59:21.316868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c401d4de4bbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('employee_count', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('specialities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('picture', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('vacancies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('skills', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('salary_min', sa.String(), nullable=True),
    sa.Column('salary_max', sa.String(), nullable=True),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.Column('speciality_code', sa.String(), nullable=True),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['company_name'], ['companies.name'], ),
    sa.ForeignKeyConstraint(['speciality_code'], ['specialities.code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies')
    op.drop_table('specialities')
    op.drop_table('companies')
    # ### end Alembic commands ###
