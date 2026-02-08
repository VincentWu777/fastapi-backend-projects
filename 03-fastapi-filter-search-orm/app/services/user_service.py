from sqlalchemy.orm import Session

from ..repositories import user_repository
from ..schemas import UserFilterQuery


def list_users(
        session: Session,
        *,
        filters: UserFilterQuery,
        limit: int,
        offset: int,
):
    items, total = user_repository.list_users(
        session,
        filters=filters,
        limit=limit,
        offset=offset,
    )

    return items, total