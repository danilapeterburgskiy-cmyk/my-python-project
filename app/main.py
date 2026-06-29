import sys
import os

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db import crud

def main():
    """Главная функция для вывода данных из БД"""
    
    db = SessionLocal()
    
    try:
        print("=" * 60)
        print("КНИГИ И КАТЕГОРИИ")
        print("=" * 60)
        
        # Получение всех категорий
        categories = crud.get_categories(db)
        print(f"\nВсего категорий: {len(categories)}")
        
        for category in categories:
            print(f"\n📚 КАТЕГОРИЯ: {category.title} (ID: {category.id})")
            print("-" * 50)
            
            # Получение книг по категории
            books = crud.get_books_by_category(db, category.id)
            print(f"Книг в категории: {len(books)}")
            
            for book in books:
                print(f"  📖 {book.title}")
                print(f"     Описание: {book.description}")
                print(f"     Цена: {book.price:.2f} руб.")
                if book.url:
                    print(f"     URL: {book.url}")
                print()
        
        # Общая статистика
        all_books = crud.get_books(db)
        print("\n" + "=" * 60)
        print(f"ИТОГО: {len(all_books)} книг в {len(categories)} категориях")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()