from psycopg import Connection
from psycopg.errors import UniqueViolation


def create_user(
    conn: Connection,
    *,
    name: str,
    email: str,
) -> dict:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id, name, email
            """,
            (name, email),
        )
        row = cur.fetchone()
        assert row is not None

        user_id, user_name, user_email = row
        return {
            "id": user_id,
            "name": user_name,
            "email": user_email,
        }


def update_user(
    conn: Connection,
    *,
    user_id: int,
    name: str | None,
    email: str | None,
) -> dict | None:
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE users
            SET
                name = COALESCE(%s, name),
                email = COALESCE(%s, email)
            WHERE id = %s
            RETURNING id, name, email
            """,
            (name, email, user_id),
        )
        row = cur.fetchone()
        if row is None:
            return None

        uid, name, email = row
        return {"id": uid, "name": name, "email": email}
