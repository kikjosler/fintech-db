-- Пользователи
INSERT INTO users (name, email) VALUES
    ('Иван', 'ivan@example.com'),
    ('Мария', 'maria@example.com'),
    ('Алексей', 'alex@example.com');

-- Счета
INSERT INTO accounts (user_id, balance) VALUES
    (1, 5000.00),
    (1, 10000.00),
    (2, 7500.00),
    (3, 3000.00),
    (2, 2000.00);