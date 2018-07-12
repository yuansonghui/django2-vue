
from mysite import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool


Base = declarative_base()


def get_session(autocommit=True, expire_on_commit=False):
    """Return a SQLAlchemy session."""

    engine = create_engine(settings.MYSQL_PATH, poolclass=NullPool)
    _SESSION_MAKER = sessionmaker(bind=engine, autocommit=True, expire_on_commit=False)
    session = scoped_session(_SESSION_MAKER)
    return session


def model_query(cls, session=None):
    if not session:
        session = get_session()
    query = session.query(cls)
    return query
