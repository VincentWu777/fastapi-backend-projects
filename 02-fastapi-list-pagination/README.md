# 02-fastapi-list-pagination

FastAPI project focused on **list (collection) API design** with pagination.

---

## Focus

- `GET /users`
- Pagination with `limit` / `offset`
- Collection response with metadata

---

## Key Ideas

- Collection APIs are not simple arrays
- Empty lists are valid results
- Pagination is part of the API contract

---

## Architecture

Router → Service → Repository → Database


---

## Stack

FastAPI · PostgreSQL · psycopg3

---

## Status

✅ Complete