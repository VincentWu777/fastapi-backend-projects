from psycopg import AsyncConnection
from psycopg.errors import UniqueViolation

from ..repositories import user_repository


class UserAlreadyExists(Exception):
    pass


async def create_user(
    conn: AsyncConnection,
    *,
    name: str,
    email: str,
) -> dict:
    try:

        return await user_repository.create_user(
            conn,
            name=name,
            email=email,
        )
    except UniqueViolation as exc:

        raise UserAlreadyExists() from exc
