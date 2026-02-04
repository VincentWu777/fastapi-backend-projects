from __future__ import annotations

from typing import AsyncGenerator

from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool

from .settings import settings

pool: AsyncConnectionPool | None = None


async def init_db() -> None:
    global pool
    pool = AsyncConnectionPool(
        conninfo=settings.database_url,
        min_size=1,
        max_size=10,
        open=False,
    )
    await pool.open()


async def close_db() -> None:
    global pool
    if pool is not None:
        await pool.close()
        pool = None


async def get_connection() -> AsyncGenerator[AsyncConnection, None]:
    if pool is None:
        raise RuntimeError("Database pool not initialized")

    async with pool.connection() as conn:
        async with conn.transaction():

            yield conn

