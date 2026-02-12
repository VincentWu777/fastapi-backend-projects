from sqlalchemy import select, func
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserFilterQuery, UserSortQuery


SORT_COLUM_MAP = {
    "id": User.id,
    "name": User.name,
    "email": User.email,
}


def list_users(
        session: Session,
        *,
        filters: UserFilterQuery,
        sorting: UserSortQuery,
        limit: int,
        offset: int,
):
    base_stmt = select(User)

    #filters
    if filters.name is not None:
        base_stmt = base_stmt.where(User.name.ilike(f"%{filters.name}%"))

    if filters.email is not None:
        base_stmt = base_stmt.where(User.email.ilike(f"%{filters.email}%"))

    #sorting
    sort_colum = SORT_COLUM_MAP[sorting.sort_by]

    if sorting.order == "asc":
        base_stmt = base_stmt.order_by(sort_colum.asc())
    else:
        base_stmt = base_stmt.order_by(sort_colum.desc())

    #total
    count_stmt = select(func.count()).select_from(
        base_stmt.subquery()
    )
    total = session.execute(count_stmt).scalar_one()

    #items
    items_stmt = (
        base_stmt
        .limit(limit)
        .offset(offset)
    )

    items = session.execute(items_stmt).scalars().all()

    return items, total