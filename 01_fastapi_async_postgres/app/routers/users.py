from fastapi import APIRouter, Depends, HTTPException, status
from psycopg import AsyncConnection

from ..database import get_connection
from ..schemas import UserCreate, UserOut
from ..services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    payload: UserCreate,
    conn: AsyncConnection = Depends(get_connection),
):
    try:
        return await user_service.create_user(
            conn,
            name=payload.name,
            email=str(payload.email),
        )
    except user_service.UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
