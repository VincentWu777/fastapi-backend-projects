from fastapi import APIRouter, HTTPException, status

from ..database import get_connection
from ..schemas import UserCreate, UserOut, UserUpdate
from ..services import user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def list_users():
    return {"message": "todo"}


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
                email=str(payload.email),
            )
    except user_service.UserAlreadyExist:
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


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, payload: UserUpdate):
    try:
        with get_connection() as conn:
            return user_service.update_user(
                conn,
                user_id=user_id,
                name=payload.name,
                email=payload.email,
            )
    except user_service.UserNotFound:
        raise HTTPException(404, "User not found")
    except user_service.UserAlreadyExist:
        raise HTTPException(409, "User already exists")


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    try:
        with get_connection() as conn:
            user_service.delete_user(conn, user_id=user_id)
    except user_service.UserNotFound:
        raise HTTPException(404, "User not found")