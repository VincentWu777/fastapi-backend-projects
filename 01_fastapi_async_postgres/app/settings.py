from pydantic import BaseModel


class Settings(BaseModel):
    database_url: str = "postgresql://fastapi_user:fastapi_password@localhost:5432/fastapi_db"


settings = Settings()
