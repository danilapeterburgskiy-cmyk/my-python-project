## Полный текст README.md (общий, без разделения на задания)

```markdown
# My Python Project

Проект по настройке среды разработки Python, работе с PostgreSQL и созданию API на FastAPI.

---

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/danilapeterburgskiy-cmyk/my-python-project.git
cd my-python-project
```

### 2. Создание и активация виртуального окружения
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

Создайте файл `.env` в корне проекта:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

Убедитесь, что PostgreSQL запущен и создан пользователь `octagon` с базой данных `octagon_db`.

### 5. Инициализация базы данных
```bash
python3 app/init_db.py
```

---

## Запуск приложения

### Запуск через терминал (вывод данных из БД)
```bash
python3 app/main.py
```

### Запуск API сервера
```bash
uvicorn app.main:app --reload
```

Сервер запустится на http://127.0.0.1:8000

---

## API Эндпоинты

### Swagger документация
http://127.0.0.1:8000/docs

### Health Check
- **GET** `/health` — проверка работоспособности сервиса

### Категории
- **GET** `/categories/` — список всех категорий
- **GET** `/categories/{id}` — получение категории по ID
- **POST** `/categories/` — создание категории
- **PUT** `/categories/{id}` — обновление категории
- **DELETE** `/categories/{id}` — удаление категории

### Книги
- **GET** `/books/` — список всех книг (с фильтром по `?category_id=`)
- **GET** `/books/{id}` — получение книги по ID
- **POST** `/books/` — создание книги
- **PUT** `/books/{id}` — обновление книги
- **DELETE** `/books/{id}` — удаление книги

---

## Примеры запросов

### Создание категории
```bash
curl -X POST "http://127.0.0.1:8000/categories/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Фантастика"}'
```

### Создание книги
```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Дюна",
    "description": "Научно-фантастический роман",
    "price": 650.00,
    "category_id": 1,
    "url": ""
  }'
```

### Получение всех книг
```bash
curl -X GET "http://127.0.0.1:8000/books/"
```

### Получение книг по категории
```bash
curl -X GET "http://127.0.0.1:8000/books/?category_id=1"
```

### Получение всех категорий
```bash
curl -X GET "http://127.0.0.1:8000/categories/"
```

### Обновление категории
```bash
curl -X PUT "http://127.0.0.1:8000/categories/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Научная фантастика"}'
```

### Обновление книги
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Дюна: Обновленное издание",
    "price": 750.00
  }'
```

### Удаление категории
```bash
curl -X DELETE "http://127.0.0.1:8000/categories/1"
```

### Удаление книги
```bash
curl -X DELETE "http://127.0.0.1:8000/books/1"
```
---

## Технологии

- **Python 3** — язык программирования
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM для работы с БД
- **FastAPI** — фреймворк для создания API
- **Uvicorn** — ASGI сервер
- **Pydantic** — валидация данных
- **python-dotenv** — управление переменными окружения
