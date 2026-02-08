# 03-fastapi-filter-search

FastAPI project focused on **filter / search query modeling** using SQLAlchemy.

---

## Focus

- `GET /users` with optional filters
- Query Object–based filtering
- SQLAlchemy used **only** in the repository layer

---

## Key Ideas

- Filters are part of the API contract
- Query conditions are modeled, not scattered
- ORM is an implementation detail, not an architectural center

---

## Architecture

Router → Service → Repository → ORM → Database


---

## Stack

FastAPI · PostgreSQL · SQLAlchemy · Pydantic

---

## Status

✅ Complete