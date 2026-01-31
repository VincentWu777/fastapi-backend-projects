# Project 01 — Pydantic Contracts

## Purpose

This project focuses on understanding **API contracts** in FastAPI using Pydantic.

Instead of starting with databases or business logic, the goal is to first define:
- what data the API is allowed to accept
- what data the API is allowed to return
- how invalid requests are rejected at the system boundary

This establishes a clear and enforceable interface between clients and the backend.

---

## What This Project Covers

### 1. Input and Output Contracts

Two separate Pydantic models are used:

- `UserCreate`: defines the request body for creating a user
- `UserPublic`: defines the response body returned to the client

Input and output schemas are intentionally separated to prevent sensitive data (e.g. passwords) from being exposed.

---

### 2. Validation at the API Boundary

Request validation is handled automatically by FastAPI using Pydantic **before** the route function is executed.

This means:
- invalid data never reaches application logic
- validation rules are centralized in schema definitions
- route handlers can assume valid, well-typed input

---

### 3. Structural Safety with `response_model`

The `response_model` parameter ensures that only explicitly allowed fields are included in the response.

Even if internal data contains additional fields, they are structurally excluded from the API response.

---

### 4. Unified Validation Error Handling

Default FastAPI validation errors are intercepted and transformed into a unified error format.

This ensures:
- consistent error responses across endpoints
- clear separation between framework behavior and system behavior
- a foundation for extending error handling in later projects

---

## Outcome

After completing this project, the API layer has:

- explicit input and output contracts
- automatic request validation
- structurally safe responses
- consistent validation error handling

This project establishes the foundation for all subsequent backend system design and development.
