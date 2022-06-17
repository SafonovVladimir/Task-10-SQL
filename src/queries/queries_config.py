from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://yaxqouiimjpmtm:6617a1c5caa35b46e75a6172a44c51cad90d9d77b89f777e196194a13cc4'
                       '52e5@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d6hf47p3m72qto')
# engine = create_engine('postgresql://admin:admin@localhost:5432/uni')
conn = engine.connect()
Session = sessionmaker(bind=engine, expire_on_commit=False, )


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
