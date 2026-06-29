import sys
import os

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import books, categories
from app.db.db import engine, Base, SessionLocal
from app.db import crud

# ============================================================
# ЗАДАНИЕ 4: Hello, World! (запуск как обычный скрипт)
# ============================================================

def zadanie_4():
    """Функция для задания 4 - вывод Hello, world!"""
    print("=" * 60)
    print("ЗАДАНИЕ 4: Hello, World!")
    print("=" * 60)
    print("Hello, world!")
    print()

# ============================================================
# ЗАДАНИЕ 5: Работа с базой данных (запуск как обычный скрипт)
# ============================================================

def zadanie_5():
    """Функция для задания 5 - вывод данных из БД"""
    print("=" * 60)
    print("ЗАДАНИЕ 5: КНИГИ И КАТЕГОРИИ")
    print("=" * 60)
    
    db = SessionLocal()
    try:
        categories_list = crud.get_categories(db)
        print(f"\nВсего категорий: {len(categories_list)}")
        
        for category in categories_list:
            print(f"\n📚 КАТЕГОРИЯ: {category.title} (ID: {category.id})")
            print("-" * 50)
            
            books_list = crud.get_books_by_category(db, category.id)
            print(f"Книг в категории: {len(books_list)}")
            
            for book in books_list:
                print(f"  📖 {book.title}")
                print(f"     Описание: {book.description}")
                print(f"     Цена: {book.price:.2f} руб.")
                if book.url:
                    print(f"     URL: {book.url}")
                print()
        
        all_books = crud.get_books(db)
        print("\n" + "=" * 60)
        print(f"ИТОГО: {len(all_books)} книг в {len(categories_list)} категориях")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
    finally:
        db.close()

# ============================================================
# ЗАДАНИЕ 6: FastAPI (запуск через uvicorn)
# ============================================================

# Создание таблиц (если их нет)
Base.metadata.create_all(bind=engine)

# Создание приложения FastAPI
app = FastAPI(
    title="Books API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

# Настройка CORS (для доступа из браузера)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров из задания 6
app.include_router(books.router)
app.include_router(categories.router)

# Эндпоинт для проверки работоспособности (задание 6)
@app.get("/health")
def health_check():
    """Проверка работоспособности сервиса"""
    return {"status": "ok", "message": "Service is running"}

# ============================================================
# Точка входа при запуске как обычный скрипт (задания 4 и 5)
# ============================================================

if __name__ == "__main__":
    import sys
    
    # Запуск заданий 4 и 5 при прямом запуске python app/main.py
    zadanie_4()
    zadanie_5()