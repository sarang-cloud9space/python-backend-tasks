-- Query 1: Retrieve all users
SELECT *
FROM users;

-- Query 2: Find a user by email
SELECT *
FROM users
WHERE email = 'amit@example.com';

-- Query 3: Get the 3 most expensive expenses
SELECT description, amount
FROM expenses
ORDER BY amount DESC
LIMIT 3;

SELECT * FROM expenses;

-- Query 4: Add a new expense
INSERT INTO expenses
    (user_id, category_id, amount, description, expense_date)
VALUES
    (1, 1, 75.00, 'Tea and snacks', CURRENT_DATE);

-- Query 5: Update an expense amount
UPDATE expenses
SET amount = 85.00
WHERE description = 'Tea and snacks'
  AND user_id = 1;

-- Query 6: Delete an expense
DELETE FROM expenses
WHERE description = 'Tea and snacks'
  AND user_id = 1
RETURNING *;

-- Query 7: Show expenses with user and category names
SELECT
    users.name AS user_name,
    categories.name AS category,
    expenses.description,
    expenses.amount
FROM expenses
INNER JOIN users
    ON expenses.user_id = users.id
INNER JOIN categories
    ON expenses.category_id = categories.id
ORDER BY expenses.amount DESC;

-- Query 8: Calculate total spending by category
SELECT
    categories.name AS category,
    SUM(expenses.amount) AS total_spent
FROM expenses
INNER JOIN categories
    ON expenses.category_id = categories.id
GROUP BY categories.name
ORDER BY total_spent DESC;

-- Query 9: Find categories with total spending above ₹500
SELECT
    categories.name AS category,
    SUM(expenses.amount) AS total_spent
FROM expenses
INNER JOIN categories
    ON expenses.category_id = categories.id
GROUP BY categories.name
HAVING SUM(expenses.amount) > 500
ORDER BY total_spent DESC;

-- Query 10: Show all users and their expenses, if any
SELECT
    users.name AS user_name,
    expenses.description,
    expenses.amount
FROM users
LEFT JOIN expenses
    ON users.id = expenses.user_id
ORDER BY users.name;

-- Indexes to speed up lookups by user and category
CREATE INDEX idx_expenses_user_id
ON expenses(user_id);

CREATE INDEX idx_expenses_category_id
ON expenses(category_id);