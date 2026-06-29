from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, unique=True)
    
    # Связь с книгами
    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float)
    url = Column(String(500), default="")
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    # Связь с категорией
    category = relationship("Category", back_populates="books")