# User Management API

A production-style backend project built with **FastAPI** following clean architecture principles.
This project implements a secure user registration system with password hashing, validation, and database persistence using PostgreSQL.

---

## 🚀 Tech Stack

* Python 3
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic (validation)
* Passlib (bcrypt password hashing)
* Uvicorn (ASGI server)

---

## 📂 Project Structure

```
app/
│
├── api/            # Routes / Controllers
├── core/           # Security & configuration
├── db/             # Database connection & session
├── models/         # SQLAlchemy models (tables)
├── schemas/        # Pydantic validation schemas
├── repositories/   # Database queries
├── services/       # Business logic
└── main.py         # Application entry point
```

---

## ⚙️ Features

* User Registration API
* Password hashing (bcrypt)
* Input validation using Pydantic
* Clean layered architecture
* PostgreSQL database integration
* Swagger API documentation

---

## 🔐 API Endpoint

### Register User

`POST /users/`

Example Request:

```json
{
  "email": "user@example.com",
  "password": "admin123"
}
```

Example Response:

```json
{
  "id": 1,
  "email": "user@example.com",
  "is_active": true,
  "is_admin": false
}
```

---

## 🧠 Architecture Overview

The project follows a layered backend architecture:

Client → API Routes → Services → Repositories → Database

Each layer has a single responsibility:

* **API**: Handles HTTP requests
* **Service**: Business logic & validation
* **Repository**: Database operations
* **Model**: Database schema

---

## 🛠 Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/yourusername/user-management-api.git
cd user-management-api
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/usermanagement
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run Server

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Notes

This project is part of a backend engineering learning journey focused on understanding real-world API design, security, and scalable architecture rather than building a simple CRUD tutorial project.

---

## 👨‍💻 Author

Ujjal Banik
MCA | Backend Developer (Python)
