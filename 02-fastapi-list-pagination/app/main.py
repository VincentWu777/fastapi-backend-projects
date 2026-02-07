from fastapi import FastAPI

from .routers import users

app = FastAPI(title="FastAPI CRUD with PostgreSQL")

app.include_router(users.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
