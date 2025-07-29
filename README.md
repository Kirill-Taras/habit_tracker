# 🧠 Habit Tracker

Habit Tracker — это backend-сервис для отслеживания и управления полезными привычками. Пользователи могут создавать свои привычки, отмечать приятные, устанавливать периодичность и время выполнения, а также делиться публичными привычками с другими. Проект включает напоминания через Telegram и отложенные задачи с Celery.

## 🚀 Функциональность

- Регистрация и аутентификация по email (JWT)
- Управление привычками: создание, просмотр, редактирование, удаление
- Разделение на приятные и полезные привычки
- Поддержка связанных привычек и вознаграждений
- Публичные привычки, доступные без авторизации
- Напоминания через Telegram бот
- Отложенные задачи через Celery
- API-документация Swagger/Redoc

## 🛠 Используемые технологии

- Python 3.10+
- Django 4+
- Django REST Framework
- PostgreSQL
- Celery + Redis
- Telegram Bot API
- JWT (SimpleJWT)
- drf-yasg (Swagger/OpenAPI)
- dotenv
- Flake8 (линтинг)
- Pytest / Django Test Framework

## 📦 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ТВОЙ_GITHUB/habit_tracker.git
cd habit_tracker
```

### 2.активировать виртуальное окружение
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate     # для Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения

### 5. Применить миграции и создать суперпользователя

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Запустить Celery и Redis

### 7. Запустить сервер Django
```bash
python manage.py runserver
```

🧑‍💻 Автор
Разработчик: Кирилл Тарасов

Telegram: @tarasov1792