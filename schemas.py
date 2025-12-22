from pydantic import BaseModel,EmailStr 
from datetime import date
from typing import Optional
class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str]
    price: float
    stock: int
    genre: Optional[str]
    published_date: Optional[date]
    description: Optional[str]

class BookCreate(BookBase): pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    isbn: Optional[str]
    price: Optional[float]
    stock: Optional[int] 
    genre: Optional[str]
    published_date: Optional[date]
    description: Optional[str]

class BookOut(BookBase):
    id: int
    class Config: orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config: orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

