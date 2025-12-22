from sqlalchemy import Column,Integer,String,Float,Date,Text
from database import Base
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    isbn = Column(String(32), unique=True, nullable=True, index=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    genre = Column(String(100), nullable=True, index=True)
    published_date = Column(Date, nullable=True)
    description = Column(Text, nullable=True)
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,index=True,nullable=False)
    email=Column(String(100),unique=True,index=True,nullable=False)
    hashed_password=Column(String(255),nullable=False)

    