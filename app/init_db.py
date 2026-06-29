import sys
import os

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal, engine, Base
from app.db import models, crud

def init_database():
    """Инициализация базы данных и добавление тестовых данных"""
    
    # Создание таблиц
    Base.metadata.create_all(bind=engine)
    
    # Создание сессии
    db = SessionLocal()
    
    try:
        # Проверяем, есть ли уже категории
        existing_categories = crud.get_categories(db)
        if existing_categories:
            print("База данных уже содержит данные. Пропускаем инициализацию.")
            return
        
        print("Добавление категорий...")
        
        # Создание категорий
        fiction = crud.create_category(db, "Художественная литература")
        science = crud.create_category(db, "Научная литература")
        children = crud.create_category(db, "Детская литература")
        
        print(f"Созданы категории: {fiction.title}, {science.title}, {children.title}")
        
        # Добавление книг для категории "Художественная литература"
        books_data = [
            {
                "title": "Мастер и Маргарита",
                "description": "Роман Михаила Булгакова",
                "price": 450.00,
                "category_id": fiction.id
            },
            {
                "title": "Преступление и наказание",
                "description": "Роман Фёдора Достоевского",
                "price": 390.00,
                "category_id": fiction.id
            },
            {
                "title": "Война и мир",
                "description": "Роман Льва Толстого",
                "price": 550.00,
                "category_id": fiction.id
            },
            # Книги для категории "Научная литература"
            {
                "title": "Краткая история времени",
                "description": "Стивен Хокинг о вселенной",
                "price": 670.00,
                "category_id": science.id
            },
            {
                "title": "Сознание и мозг",
                "description": "Как мозг создает сознание",
                "price": 520.00,
                "category_id": science.id
            },
            # Книги для категории "Детская литература"
            {
                "title": "Маленький принц",
                "description": "Антуан де Сент-Экзюпери",
                "price": 320.00,
                "category_id": children.id
            },
            {
                "title": "Винни-Пух",
                "description": "Приключения медвежонка",
                "price": 280.00,
                "category_id": children.id
            },
            {
                "title": "Малыш и Карлсон",
                "description": "Астрид Линдгрен",
                "price": 350.00,
                "category_id": children.id
            }
        ]
        
        print("Добавление книг...")
        for book_data in books_data:
            book = crud.create_book(db, **book_data)
            print(f"  Добавлена книга: {book.title}")
        
        print("\nИнициализация базы данных завершена успешно!")
        
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()