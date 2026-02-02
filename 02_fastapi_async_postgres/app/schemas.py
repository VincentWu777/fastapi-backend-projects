from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    age: int | None = Field(default=None, ge=0, le=130)


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    age: int | None = None
