# 🏦 Fintech SQL Practice (PyCharm)

Проект для практики **базовых SQL-запросов**: SELECT, JOIN, WHERE, GROUP BY.

## Стек

- PostgreSQL 16
- Docker Compose
- Python 3.10+
- PyCharm
- psycopg2

## Запуск

### 1. Запустить PostgreSQL

```bash
docker-compose up -d
```

### 2. Установить зависимости Python

```bash
cd python
pip install -r requirements.txt
```

### 3. Запустить скрипт

```bash
python db_queries.py
```

Или в PyCharm:
- Нажми `Run` → `Run 'db_queries'`

### 4. Подключиться к БД вручную

```bash
docker exec -it fintech-db psql -U postgres -d fintech
```

## Практика SQL

Открой `sql/01_schema.sql` и `sql/02_seed_data.sql` — там простые таблицы для практики.

Попробуй выполнить эти запросы в `psql`:

```sql
-- Показать всех пользователей
SELECT * FROM users;

-- Пользователь и баланс (JOIN)
SELECT u.name, a.balance
FROM users u
JOIN accounts a ON u.id = a.user_id;

-- Общий баланс (GROUP BY)
SELECT u.name, SUM(a.balance) as total
FROM users u
JOIN accounts a ON u.id = a.user_id
GROUP BY u.id, u.name;
```
