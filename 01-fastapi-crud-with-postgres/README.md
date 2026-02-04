# 01-fastapi-crud-with-postgres

A foundational FastAPI project for learning **correct CRUD backend design**
using PostgreSQL.

## Goals

- Understand the separation between Router / Service / Repository
- Learn proper HTTP status code semantics (201, 404, 409)
- Use PostgreSQL constraints as the source of truth
- Build a backend that is correct before making it async

## Tech Stack

- FastAPI
- PostgreSQL
- psycopg3 (sync)
- Pydantic

## Scope

This project intentionally avoids async and connection pools.
The focus is correctness, clarity, and backend fundamentals.
