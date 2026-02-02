from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

# Global async connection pool
pool = AsyncConnectionPool(
    conninfo=DATABASE_URL,
    min_size=1,
    max_size=5,
)


async def init_db():
    """
    Initialize database schema (async).
    """
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    email TEXT NOT NULL UNIQUE,
                    age INTEGER
                )
                """
            )
