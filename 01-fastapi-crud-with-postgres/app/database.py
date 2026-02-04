import psycopg
from psycopg import Connection
from contextlib import contextmanager

DATABASE_URL = "postgresql://fastapi_user:fastapi_password@localhost:5432/fastapi_db"


@contextmanager
def get_connection() -> Connection:
    """
    One request = one database transaction.
    """
    conn = psycopg.connect(DATABASE_URL)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
