from typing import Literal
from pydantic import BaseModel, EmailStr, Field


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserListQuery(BaseModel):
    limit: int = Field(default=10, ge=1, le=100)
    offset: int = Field(default=0, ge=0)


class UserFilterQuery(BaseModel):
    name: str | None = None
    email: str | None = None


class UserListResponse(BaseModel):
    items: list[UserOut]
    total: int
    limit: int
    offset: int


class UserSortQuery(BaseModel):
    sort_by: Literal["id", "name", "email"] = "id"
    order: Literal["asc", "desc"] = "asc"