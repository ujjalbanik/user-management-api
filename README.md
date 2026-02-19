# User Management API (Production-Style Backend)

A production-style backend REST API built using FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.
The project follows clean architecture principles, layered design, and automated testing practices used in real backend systems.

## Features

* User registration & login
* JWT authentication (stateless auth)
* Role-based access control (Admin & User)
* Secure password hashing (bcrypt)
* Protected routes
* Ownership permissions (users can edit only themselves)
* Filtering & pagination
* Centralized error handling
* Automated API testing (pytest)
* Database migrations using Alembic

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Alembic (migrations)
* Pytest (automated testing)
* Pydantic (validation)
* Passlib (password hashing)
* Python-JOSE (JWT auth)

## Project Structure

app/

* api → route layer
* services → business logic
* repositories → database operations
* models → DB models
* schemas → validation layer
* core → security & config

## How to Run

1. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Setup environment variables
   Create `.env`:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Run migrations

```
alembic upgrade head
```

5. Start server

```
uvicorn app.main:app --reload
```

## Run Tests

```
pytest
```

## What I Learned

This project helped me understand:

* layered backend architecture
* authentication & authorization
* secure API design
* database migrations
* automated testing workflow

## 👨‍💻 Author

Ujjal Banik
MCA | Backend Developer (Python)
