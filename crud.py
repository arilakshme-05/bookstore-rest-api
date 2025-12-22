from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Book, User
from schemas import BookCreate, BookUpdate, UserCreate
from auth import hash_password

# --- Book CRUD ---
def get_book_or_404(db: Session, book_id: int) -> Book:
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def create_book(db: Session, payload: BookCreate) -> Book:
    if payload.isbn:
        existing = db.query(Book).filter(Book.isbn == payload.isbn).first()
        if existing:
            raise HTTPException(status_code=409, detail="ISBN already exists")
    book = Book(**payload.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, payload: BookUpdate) -> Book:
    book = get_book_or_404(db, book_id)
    if payload.isbn and payload.isbn != book.isbn:
        exists = db.query(Book).filter(Book.isbn == payload.isbn).first()
        if exists:
            raise HTTPException(status_code=409, detail="ISBN already exists")
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(book, k, v)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book_or_404(db, book_id)
    db.delete(book)
    db.commit()

# --- User CRUD ---
def create_user(db: Session, user: UserCreate) -> User:
    try:
        if db.query(User).filter((User.username == user.username) | (User.email == user.email)).first():
            raise HTTPException(status_code=400, detail="Username or email already registered")
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print("Registration error:", e)
        raise HTTPException(status_code=500, detail="Internal error")

