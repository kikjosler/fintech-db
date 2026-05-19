# Fintech DB

Проект для практики **базовых SQL-запросов**: SELECT, JOIN, WHERE, GROUP BY.

## Стек

- PostgreSQL 16
- Docker Compose
- Python 3.10+
- PyCharm
- psycopg2
- pgAdmin 4 (веб-интерфейс)

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
