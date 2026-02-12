#  FastAPI User Management API

A simple FastAPI-based REST API to perform CRUD operations (Create, Read, Update, Delete) on user data using in-memory storage.

---

##  Features

- Get all users
- Get user by ID
- Get user by name
- Create new user
- Update existing user
- Delete user

---

##  Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## How to Run

### Install dependencies
```bash
pip install fastapi uvicorn
```

### Run Server
```bash
uvicorn api:app --reload
```

### Open Swagger UI
```bash
http://127.0.0.1:8000/docs
```






