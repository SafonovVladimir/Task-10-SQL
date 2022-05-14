from contextlib import contextmanager
# from sqlalchemy.dialects import postgresql
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from db.models import Group, db

engine = sa.create_engine(
    # 'postgresql://admin:admin@localhost/uni',
    # 'postgres://localhost:5432/habr_sql?sslmode=disable',
    'postgres://localhost:5432/',
    echo=True,
)
conn = engine.connect()

DBSession = sessionmaker(
    binds={
        db: engine,
    },
    # bind=engine,
    expire_on_commit=False,
)


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


if __name__ == '__main__':
    with session_scope() as s:
        questions = s.query(Group).filter().order_by(Group.name.asc())
        # result = conn.execute(questions)
        # for row in result:
        #     print(row)
        # print(questions)
# print(expression.compile(dialect=postgresql.dialect()))
