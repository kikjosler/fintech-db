import os
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv

# Загрузить переменные из .env
load_dotenv()

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", 5432)),
    database=os.getenv("DB_NAME", "fintech"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "postgres123")
)

cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

print("=" * 60)
print("Fintech SQL Practice - Базовые запросы")
print("=" * 60)

# 1. Показать всех пользователей
print("\n1. Все пользователи:")
cursor.execute("SELECT id, name, email FROM users")
users = cursor.fetchall()
for user in users:
    print(f"   ID: {user['id']}, Имя: {user['name']}, Email: {user['email']}")

# 2. Показать имя пользователя и его баланс (JOIN)
print("\n2. Пользователь и баланс (JOIN):")
cursor.execute("""
    SELECT u.name, a.balance
    FROM users u
    JOIN accounts a ON u.id = a.user_id
""")
rows = cursor.fetchall()
for row in rows:
    print(f"   {row['name']}: {row['balance']} RUB")

# 3. Общий баланс по пользователю (GROUP BY)
print("\n3. Общий баланс по пользователю (GROUP BY):")
cursor.execute("""
    SELECT u.name, SUM(a.balance) as total_balance
    FROM users u
    JOIN accounts a ON u.id = a.user_id
    GROUP BY u.id, u.name
    ORDER BY total_balance DESC
""")
rows = cursor.fetchall()
for row in rows:
    print(f"   {row['name']}: {row['total_balance']} RUB")

# 4. Сколько счетов у каждого пользователя
print("\n4. Счета у каждого пользователя (COUNT):")
cursor.execute("""
    SELECT u.name, COUNT(a.id) as account_count
    FROM users u
    LEFT JOIN accounts a ON u.id = a.user_id
    GROUP BY u.id, u.name
""")
rows = cursor.fetchall()
for row in rows:
    print(f"   {row['name']}: {row['account_count']} счета")

cursor.close()
conn.close()

print("\nЗапросы выполнены!")