from psycopg import Connection

from ..repositories import user_repository


def list_users(
        conn: Connection,
        *,
        limit: int,
        offset: int,
) -> tuple[list[dict], int]:
    items, total = user_repository.list_users(
        conn,
        limit=limit,
        offset=offset,
    )

    return items, total