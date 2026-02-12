from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_session
from ..schemas import (
    UserListQuery,
    UserFilterQuery,
    UserSortQuery,
    UserListResponse,
    UserOut,
)
from ..services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=UserListResponse)
def list_users(
        pagination: UserListQuery = Depends(),
        filters: UserFilterQuery = Depends(),
        sorting: UserSortQuery = Depends(),
        session: Session = Depends(get_session),
):
    items, total = user_service.list_users(
        session,
        filters=filters,
        sorting=sorting,
        limit=pagination.limit,
        offset=pagination.offset,
    )

    return UserListResponse(
        items=[UserOut.model_validate(user) for user in items],
        total=total,
        limit=pagination.limit,
        offset=pagination.offset,
    )