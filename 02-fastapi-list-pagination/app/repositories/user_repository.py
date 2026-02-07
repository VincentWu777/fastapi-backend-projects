from psycopg import Connection


def list_users(
        conn: Connection,
        *,
        limit: int,
        offset: int,
) -> tuple[list[dict], int]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, name, email
            FROM users
            ORDER BY id
            LIMIT %s OFFSET %s
            """,
            (limit, offset),
        )
        rows = cur.fetchall()

        items = [
            {"id": uid, "name": name, "email": email}
            for uid, name, email in rows
        ]


        cur.execute(
            """
            SELECT COUNT(*)
            FROM users
            """
        )
        (total,) = cur.fetchone()

        return items, total