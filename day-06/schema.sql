CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM users;

CREATE TABLE categories (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE expenses (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    category_id INTEGER NOT NULL REFERENCES categories(id),
    amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0),
    description VARCHAR(255),
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email)
VALUES
    ('Amit Sharma', 'amit@example.com'),
    ('Priya Patil', 'priya@example.com'),
    ('Rahul Deshmukh', 'rahul@example.com');

INSERT INTO categories (name)
VALUES
    ('Food'),
    ('Travel'),
    ('Shopping'),
    ('Bills'),
    ('Health');

INSERT INTO expenses
    (user_id, category_id, amount, description, expense_date)
VALUES
    (1, 1, 250.00, 'Lunch', '2026-10-20'),
    (1, 2, 120.00, 'Bus ticket', '2026-10-21'),
    (2, 3, 1500.00, 'Shoes', '2026-10-19'),
    (2, 1, 180.00, 'Breakfast', '2026-10-22'),
    (3, 4, 999.00, 'Electricity bill', '2026-10-18'),
    (3, 5, 350.00, 'Medicines', '2026-10-22'),
    (1, 3, 800.00, 'Backpack', '2026-10-22'),
    (2, 2, 90.00, 'Auto fare', '2026-10-21'),
    (3, 1, 220.00, 'Dinner', '2026-10-20'),
    (1, 4, 1200.00, 'Internet bill', '2026-10-19');