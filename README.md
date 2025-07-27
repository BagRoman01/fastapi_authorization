## ✅ Возможности проекта (`fastapi_authorization`)

Этот проект реализует полноценную систему авторизации и конвертации валют с использованием **FastAPI**, **SQLModel**, **PostgreSQL** и современных подходов:

* 🔐 Регистрация, авторизация и выход пользователя
* ♻️ Обновление access/refresh токенов
* ✅ Проверка токена авторизации
* 💱 Получение списка валют
* 💸 Конвертация валют
* 📊 История конвертаций

Проект построен с использованием паттерна **UoW + Repository**, а также включает **миграции Alembic**, **Docker** и строгую типизацию через Pydantic v2.
Целью проекта является в первую очередь обеспечение работы аутентификации и авторизации через jwt. 
Использование стороннего API с валютами исключительно в демонстрационных целях. 

### 🧱 Архитектура приложения

* **🔄 UoW (Unit of Work)** – паттерн, инкапсулирующий все операции с базой данных в пределах одного запроса. Это упрощает управление транзакциями и откатами при ошибках.
* **📦 Repository Pattern** – паттерн, обеспечивающий абстракцию доступа к данным. Репозитории скрывают детали работы с ORM и позволяют легко подменять реализацию или писать тесты.

🧩 Использование этих паттернов позволяет:

* изолировать бизнес-логику от слоя хранения данных;
* повысить тестируемость;
* централизованно управлять транзакциями;
* проще следовать принципам SOLID.

---

## 🧱 Стек технологий

### ⚙️ Backend

* **[FastAPI](https://fastapi.tiangolo.com/)** – современный веб-фреймворк на Python для создания высокопроизводительных REST API
* **[SQLAlchemy](https://www.sqlalchemy.org/)** – мощная ORM-библиотека для работы с базами данных на Python
* **[Pydantic v2](https://docs.pydantic.dev/)** – инструмент для валидации и сериализации данных на основе аннотаций типов
* **[SQLModel](https://sqlmodel.tiangolo.com/)** – надстройка, объединяющая возможности SQLAlchemy и Pydantic для упрощённого определения моделей данных и схем, подходящих как для работы с БД, так и для API
* **[Alembic](https://alembic.sqlalchemy.org/)** – инструмент для управления миграциями схемы базы данных
* **[Asyncpg](https://github.com/MagicStack/asyncpg)** – высокопроизводительный асинхронный драйвер PostgreSQL
* **[Aiosqlite](https://github.com/omnilib/aiosqlite)** – асинхронный драйвер для SQLite (используется при тестировании)
* **[Aiohttp](https://github.com/aio-libs/aiohttp)** – асинхронный HTTP-клиент и сервер для Python, используется для внутренних запросов и асинхронного взаимодействия с API.

### 🚀 Запуск и деплой

* **[Uvicorn](https://www.uvicorn.org/)** – быстрый ASGI-сервер для разработки
* **[Docker](https://docs.docker.com/compose/)** – контейнеризация приложения и БД
* **[uv](https://github.com/astral-sh/uv)** – современный и быстрый менеджер зависимостей (альтернатива pip)


## 🚀 Быстрый старт (Docker)

1. Клонируй репозиторий:

- git clone https://github.com/BagRoman01/fastapi_authorization.git

2. Создай `.env` файл (пример ниже) или используй уже существующий.

3. Построй и запусти сервис:

- docker compose up --build

4. Открой API-документацию:

* Swagger UI: [http://localhost:8000/docs]
* 
## ⚙️ Переменные окружения (`.env`)

```env
# DATABASE
DATABASE_HOST=db_app
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_NAME=tonalyze

# AUTHENTICATION
AUTH_SECRET_KEY=
AUTH_ALGORITHM=HS256
AUTH_ACCESS_TOKEN_EXPIRE_MINUTES=1
AUTH_REFRESH_TOKEN_EXPIRE_MINUTES=28000

# FRONTEND COMMUNICATION
FRONTEND_BACKEND_CORS_ORIGINS=["http://127.0.0.1:5174","http://localhost:5174", "http://127.0.0.1:8000"]

# DEPLOYMENT
DEPLOY_HOST=127.0.0.1
DEPLOY_PORT=8000

# USING MODE
MODE=DEV

# CURRENCY (Внешняя API)
CURRENCY_API_KEY=здесь надо указать рабочий API ключ
```
---

## 🔗 Примеры API-запросов и ответов

### 🧾 1. Регистрация

`POST /auth/register`

```json
# Request body
{
  "email": "user@example.com",
  "password": "securepassword123"
  "age": 23
}
```

```json
# Response 200
{
  "email": "user@example.com"
}
```

---

### 🔑 2. Авторизация (вход)

`POST /auth/login`

```json
# Request body
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

```json
# Response 200
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IlJvbWFuMkBleGFtcGxlLmNvbSIsImV4cCI6MTc1MzYyNzk4MX0.bEi3UQUQy91ySPkrrZcepncnyD0oWlJe68lPAHKqEcc",
  "token_type": "bearer"
}
Refresh_token устанавливается в cookie.
```

---

### 🔁 3. Обновление токенов

`GET /auth/refresh`

**Headers**:

* `Cookie: refresh_token=...`
* `user-agent: ...`

```json
# Response 200
{
"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IlJvbWFuMkBleGFtcGxlLmNvbSIsImV4cCI6MTc1MzYyNzk4MX0.bEi3UQUQy91ySPkrrZcepncnyD0oWlJe68lPAHKqEcc",
  "token_type": "bearer"
}
Refresh_token устанавливается в cookie.
```

---

### 🔍 4. Проверка авторизации

`GET /auth/authorize`

**Headers**:

* `Authorization: Bearer <access_token>`
  
  Refresh_token передается в cookie.
```json
# Response 200
{
  "email": "user@example.com"
}
```

---

### 🚪 5. Выход

`POST /auth/logout`

**Headers**:

* `Cookie: refresh_token=...`
* `user-agent: ...`

```json
# Response 200
{
  "deleted_sessions": 1
}
```

---

## 💱 Работа с валютами (Зависит от внешнего API, поэтому работа с ним может измениться)

### 🌍 6. Получение списка валют

`GET /currency/all?currencies=USD,EUR`

**Headers**:

* `Authorization: Bearer <access_token>`

---

### 💳 7. Конвертация валют

`POST /currency/exchange`

**Headers**:

* `Authorization: Bearer <access_token>`

```json
# Request body
{
  "base_cur": "USD",
  "cur_to": "EUR",
  "amount": 100
}
```
---

### 📈 8. История курса валют

`POST /currency/history_exchange`

**Headers**:

* `Authorization: Bearer <access_token>`

```json
# Request body
{
  "base_cur": "EUR",
  "cur_to": "USD",
  "amount": 200,
  "date": "2024-05-01"
}
```
---
  
