from typing import Optional

from .models import UserRecord
from ..database import pool


async def create_user(email: str, age: int | None) -> int:
    """
    Persist a new user and return its generated ID.
    """
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO users (email, age)
                VALUES (%s, %s)
                RETURNING id
                """,
                (email, age),
            )
            row = await cur.fetchone()

    return row["id"]


async def get_user_by_id(user_id: int) -> Optional[UserRecord]:
    """
    Retrieve a user by ID.
    Returns None if the user does not exist.
    """
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                SELECT id, email, age
                FROM users
                WHERE id = %s
                """,
                (user_id,),
            )
            row = await cur.fetchone()

    if row is None:
        return None

    return UserRecord(
        id=row["id"],
        email=row["email"],
        age=row["age"],
    )
