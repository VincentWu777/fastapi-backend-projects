from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, status, HTTPException
from psycopg.errors import UniqueViolation, IntegrityError

from .schemas import UserCreate, UserPublic
from .database import init_db
from .repositories.user_repository import create_user, get_user_by_id


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/users",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED
)
async def create_user_endpoint(user: UserCreate, response: Response):
    try:
        user_id = await create_user(
            email=str(user.email),
            age=user.age,
        )
    except UniqueViolation:
        # email already exists
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )
    except IntegrityError:
        # other constraint violations
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user data",
        )
    except Exception:
        # unexpected database error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    # Set Location header for the newly created resource
    response.headers["Location"] = f"/users/{user_id}"

    return {
        "id": user_id,
        "email": user.email,
        "age": user.age,
    }


@app.get("/users/{user_id}", response_model=UserPublic)
async def get_user_endpoint(user_id: int):
    user = await get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return {
        "id": user.id,
        "email": user.email,
        "age": user.age,
    }