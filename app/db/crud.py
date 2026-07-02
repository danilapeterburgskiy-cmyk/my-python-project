from sqlalchemy.orm import Session
from app.db import models

# ========== CRUD для Category ==========

def create_category(db: Session, title: str):
    """Создание категории"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    """Получение категории по ID"""
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_title(db: Session, title: str):
    """Получение категории по названию"""
    return db.query(models.Category).filter(models.Category.title == title).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    """Получение всех категорий"""
    return db.query(models.Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, title: str):
    """Обновление категории"""
    db_category = get_category(db, category_id)
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
        return db_category
    return None

def delete_category(db: Session, category_id: int):
    """Удаление категории"""
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

# ========== CRUD для Book ==========

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    """Создание книги"""
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    """Получение книги по ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    """Получение всех книг"""
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, category_id: int):
    """Получение книг по категории"""
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def update_book(db: Session, book_id: int, **kwargs):
    """Обновление книги"""
    db_book = get_book(db, book_id)
    if db_book:
        for key, value in kwargs.items():
            if hasattr(db_book, key):
                setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

def delete_book(db: Session, book_id: int):
    """Удаление книги"""
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False