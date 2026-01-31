from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .schemas import UserCreate, UserPublic

app = FastAPI()

#Health check
@app.get("/health")
def health():
    return {"status": "OK"}


#create user
@app.post("/users", response_model=UserPublic)
def create_user(user: UserCreate):
    user_data = user.model_dump(exclude={"password"})
    user_data["id"] = 1

    return user_data



