# expense_tracker/main.py
import os
import json
from datetime import datetime
import matplotlib.pyplot as plt


# expense_tracker/main.py (continued)
class Expense:
    def __init__(self, amount: float, category: str, description: str):
        self.id = len(tracker.expenses) + 1
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

    def validate(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.category:
            raise ValueError("Category cannot be empty")


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        try:
            expense = Expense(amount, category, description)
            self.expenses.append(expense.__dict__)
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for expense in self.expenses:
            print(f"ID: {expense['id']}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")
            print("-" * 30)

    def calculate_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        ]

    def generate_category_pie_chart(expenses):
        # Group expenses by category
        category_totals = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount

        # Create pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(
            category_totals.values(), labels=category_totals.keys(), autopct="%1.1f%%"
        )
        plt.title("Expense Distribution by Category")
        plt.show()


# expense_tracker/main.py (final part)
def main_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Expenses by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            total = tracker.calculate_total_expenses()
            print(f"Total Expenses: ${total:.2f}")

        elif choice == "4":
            category = input("Enter category to filter: ")
            category_expenses = tracker.get_expenses_by_category(category)
            for expense in category_expenses:
                print(f"Amount: ${expense['amount']:.2f} - {expense['description']}")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


# Initialize tracker and start application
tracker = ExpenseTracker()
main_menu()
