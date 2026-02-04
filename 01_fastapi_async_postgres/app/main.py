from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import init_db, close_db
from .routers.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)


@app.get("/health")
async def health():
    return {"status": "ok"}