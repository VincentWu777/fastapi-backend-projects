from fcntl import FASYNC

from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.testing import future

DATABASE_URL = "postgresql+psycopg://vid@localhost:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()