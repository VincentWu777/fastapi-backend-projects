from psycopg import Connection
from psycopg.errors import UniqueViolation

from ..repositories import user_repository


class UserAlreadyExist(Exception):
    pass


class UserNotFound(Exception):
    pass


def create_user(
        conn: Connection,
        *,
        name: str,
        email: str,
) -> dict:
    try:
        return user_repository.create_user(
            conn,
            name=name,
            email=email,
        )
    except UniqueViolation as exc:
        raise UserAlreadyExist() from exc


def get_user_by_id(
        conn: Connection,
        *,
        user_id: int,
) -> dict:
    user = user_repository.get_user_by_id(conn, user_id=user_id)
    if user is None:
        raise UserNotFound()
    return user


def update_user(
        conn: Connection,
        *,
        user_id: int,
        name: str | None,
        email: str | None,
) -> dict:
    try:
        user = user_repository.update_user(
            conn,
            user_id=user_id,
            name=name,
            email=email,
        )
    except UniqueViolation as exc:
        raise UserAlreadyExist() from exc

    if user is None:
        raise UserNotFound()

    return user


def delete_user(conn: Connection, *, user_id: int) -> None:
    deleted = user_repository.delete_user(conn, user_id=user_id)
    if not deleted:
        raise UserNotFound()