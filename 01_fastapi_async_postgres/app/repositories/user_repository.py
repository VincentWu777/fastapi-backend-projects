from psycopg import AsyncConnection


async def create_user(
    conn: AsyncConnection,
    *,
    name: str,
    email: str,
) -> dict:
    async with conn.cursor() as cur:
        await cur.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id, name, email
            """,
            (name, email),
        )
        row = await cur.fetchone()
        assert row is not None

        user_id, user_name, user_email = row
        return {"id": user_id, "name": user_name, "email": user_email}


async def get_user_by_id(
    conn: AsyncConnection,
    *,
    user_id: int,
) -> dict | None:
    async with conn.cursor() as cur:
        await cur.execute(
            """
            SELECT id, name, email
            FROM users
            WHERE id = %s
            """,
            (user_id,),
        )
        row = await cur.fetchone()
        if row is None:
            return None

        user_id, name, email = row
        return {"id": user_id, "name": name, "email": email}
