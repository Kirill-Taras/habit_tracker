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

- Python 
- Django 
- Django REST Framework
- PostgreSQL
- Celery + Redis
- Telegram Bot API
- JWT (SimpleJWT)
- drf-yasg (Swagger/OpenAPI)
- dotenv
- Flake8 (линтинг)
- Pytest / Django Test Framework

## 📦 Установка и запуск локально

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

## 📦 Запуск через Docker (локально или на сервере)

### 1. Собрать контейнеры

```bash
docker-compose up -d --build
```

### 2.Применить миграции
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 3. Приложение будет доступно по адресу

```bash
http://localhost:8000
```

## 🚀 Деплой на сервер
```bash
Проект разворачивается в Яндекс.Облаке (Ubuntu 22.04) с помощью GitHub Actions и Docker.
Настроить сервер:
Установить Docker и Docker Compose
Создать пользователя для деплоя
Добавить публичный SSH-ключ в ~/.ssh/authorized_keys
Создать директорию для проекта (например, ~/habit_tracker)
Добавить переменные в GitHub Secrets:
SSH_KEY — приватный ключ для подключения
SSH_USER — имя пользователя на сервере
SERVER_IP — IP-адрес сервера
DOCKER_HUB_USERNAME и DOCKER_HUB_TOKEN — данные для Docker Hub
переменные окружения для .env (DB_NAME, DB_USER, DB_PASSWORD и т.д.)

При каждом push в main запускается workflow:
Сборка и пуш Docker-образа в Docker Hub
Подключение к серверу по SSH
Обновление .env на сервере
Запуск контейнера с новой версией приложения
```


🧑‍💻 Автор
Разработчик: Кирилл Тарасов

Telegram: @tarasov1792