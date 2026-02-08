from sqlalchemy import select, func
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserFilterQuery


def list_users(
        session: Session,
        *,
        filters: UserFilterQuery,
        limit: int,
        offset: int,
):
    # ===== base query =====
    base_stmt = select(User)

    if filters.name is not None:
        base_stmt = base_stmt.where(User.name.ilike(f"%{filters.name}%"))

    if filters.email is not None:
        base_stmt = base_stmt.where(User.email.ilike(f"%{filters.email}%"))

    # ===== total =====
    count_stmt = select(func.count()).select_from(
        base_stmt.subquery()
    )

    total = session.execute(count_stmt).scalar_one()

    # ===== items =====
    items_stmt = (
        base_stmt
        .order_by(User.id)
        .limit(limit)
        .offset(offset)
    )

    items = session.execute(items_stmt).scalars().all()

    return items, total
