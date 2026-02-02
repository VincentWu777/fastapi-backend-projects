# Project 02 – FastAPI Async + PostgreSQL

This project focuses on building a **production-oriented FastAPI backend**
using **async I/O** and **PostgreSQL**.

## What this project covers

- FastAPI request / response semantics
- Async programming with `async` / `await`
- PostgreSQL integration using **psycopg3 (async)**
- Async connection pooling
- Repository pattern (SQL separated from HTTP layer)
- Clear type boundaries (API schemas vs persistence models)
- Database error → HTTP error mapping

## Key design principles

- HTTP layer only handles protocol semantics
- Repository layer only handles data access
- No ORM (SQL is explicit and intentional)
- Async used **only** at I/O boundaries

## Tech stack

- FastAPI
- PostgreSQL
- psycopg3 (async + pool)
- Pydantic

## Status

✅ Completed  
This project represents a **solid foundation for production FastAPI services**.
