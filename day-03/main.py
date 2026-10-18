from pathlib import Path
import json
from datetime import date

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "expenses.json"

print(DATA_FILE)

def initialize_file():
    if not DATA_FILE.exists():
        initial_expenses = []

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(initial_expenses, file, indent=4)

        print("Expense file created.")
    else:
        print("Expense file already exists.")


def load_expenses():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

        return expenses

    except json.JSONDecodeError:
        print("Error: expenses.json contains invalid JSON.")
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully.")



def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"Title: {expense['title']} | "
            f"Amount: ₹{expense['amount']} | "
            f"Category: {expense['category']} | "
            f"Date: {expense['date']}"
        )



def add_expense(expenses):
    title = input("Enter expense title: ").strip()

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    except ValueError as error:
        print(f"Invalid amount: {error}")
        return

    category = input("Enter expense category: ").strip()

    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")
    title = input("Enter expense title: ").strip()
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ").strip()

    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully.")

initialize_file()

expenses = load_expenses()

add_expense(expenses)

display_expenses(expenses)

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spending: ₹{total:.2f}")

calculate_total(expenses)
