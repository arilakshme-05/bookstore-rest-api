#  Bookstore REST API

A modular backend project built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.  
This API allows users to register, log in, and manage books with full CRUD functionality.  
Swagger UI is included for easy testing and documentation.

---

##  Features
- User registration and login with secure password hashing
- JWT-based authentication and protected endpoints
- CRUD operations for books (create, read, update, delete)
- Modular project structure (`models.py`, `schemas.py`, `crud.py`, `auth.py`, `main.py`)
- SQLite database (`books.db`) for persistence
- Interactive API docs via Swagger UI (`/docs`)

---

## Tools & Technologies
- **Python 3.11+**
- **FastAPI** (web framework)
- **SQLAlchemy** (ORM)
- **SQLite** (database)
- **Passlib & bcrypt** (password hashing)
- **Python-JOSE** (JWT handling)
- **Uvicorn** (ASGI server)

---

##  Setup Instructions

1. Clone the repository:
   git clone https://github.com/arilakshme-05/bookstore-rest-api.git
   cd bookstore-rest-api

2.Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run the server:
uvicorn bookstore_api.main:app --reload

5.Open Swagger UI:
Visit: http://127.0.0.1:8000/docs
