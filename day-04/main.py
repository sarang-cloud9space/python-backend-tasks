from dataclasses import dataclass
from datetime import date
from pathlib import Path
import json


@dataclass
class Expense:
    id: int
    title: str
    amount: float
    category: str
    date: str

class ExpenseTracker:
    def __init__(self, data_file):
        self.data_file = Path(data_file)
        self.expenses = []

    def initialize_file(self):
        if not self.data_file.exists():
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def load_expenses(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.expenses = [
            Expense(**item) for item in data
            ]

        except json.JSONDecodeError:
            raise ValueError("expenses.json contains invalid JSON.")

    def save_expenses(self):
        data = [
        {
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date,
        }
        for expense in self.expenses
        ]

        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_expense(self):
        title = input("Enter expense title: ").strip()

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

        except ValueError as error:
            print(f"Invalid amount: {error}")
            return

        category = input("Enter expense category: ").strip()

        expense = Expense(
            id=max((item.id for item in self.expenses), default=0) + 1,
            title=title,
            amount=amount,
            category=category,
            date=date.today().isoformat()
        )

        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully.")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for expense in self.expenses:
            print(
                f"ID: {expense.id} | "
                f"Title: {expense.title} | "
                f"Amount: ₹{expense.amount:.2f} | "
                f"Category: {expense.category} | "
                f"Date: {expense.date}"
            )

    def calculate_total(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total spending: ₹{total:.2f}")

def main():
    data_file = Path(__file__).resolve().parent / "expenses.json"

    tracker = ExpenseTracker(data_file)

    tracker.initialize_file()
    tracker.load_expenses()


    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Calculate total spending")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.display_expenses()

        elif choice == "3":
            tracker.calculate_total()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()