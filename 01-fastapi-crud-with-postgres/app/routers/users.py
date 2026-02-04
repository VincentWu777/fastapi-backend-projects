from fastapi import APIRouter, HTTPException, status

from ..database import get_connection
from ..schemas import UserCreate, UserOut
from ..services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(payload: UserCreate):
    try:
        with get_connection() as conn:
            return user_service.create_user(
                conn,
                name=payload.name,
                email=payload.email,
            )
    except user_service.UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )


@router.get(
    "/{user_id}",
    response_model=UserOut,
)
def get_user(user_id: int):
    try:
        with get_connection() as conn:
            return user_service.get_user_by_id(conn, user_id=user_id)
    except user_service.UserNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
