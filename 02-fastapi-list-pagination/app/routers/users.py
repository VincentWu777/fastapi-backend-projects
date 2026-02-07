from fastapi import APIRouter, Depends

from ..database import get_connection
from ..schemas import UserListQuery, UserListResponse
from ..services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=UserListResponse)
def list_users(
        query: UserListQuery = Depends(),
):
    with get_connection() as conn:
        items, total = user_service.list_users(
            conn,
            limit=query.limit,
            offset=query.offset,
        )

    return UserListResponse(
        items=items,
        total=total,
        limit=query.limit,
        offset=query.offset,
    )