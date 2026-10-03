"""A small command-line expense tracker using a local CSV file."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDNAMES = ["date", "category", "description", "amount"]


def load_expenses():
    """Read saved expenses from the CSV file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except OSError as error:
        print(f"Could not read saved expenses: {error}")
        return []


def save_expense(expense):
    """Append one expense to the CSV file, adding headers if needed."""
    file_exists = DATA_FILE.exists()
    try:
        with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            if not file_exists or DATA_FILE.stat().st_size == 0:
                writer.writeheader()
            writer.writerow(expense)
        return True
    except OSError as error:
        print(f"Could not save the expense: {error}")
        return False


def ask_amount():
    """Ask for a positive amount and return it as a Decimal."""
    while True:
        raw_amount = input("Amount (e.g. 12.50): ").strip().replace(",", ".")
        try:
            amount = Decimal(raw_amount)
            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return amount.quantize(Decimal("0.01"))
        except InvalidOperation:
            print("That amount is not valid. Try something like 12.50.")


def add_expense():
    """Collect expense details and save them."""
    category = input("Category (e.g. food, transport): ").strip()
    description = input("Description: ").strip()
    if not category or not description:
        print("Category and description cannot be empty.")
        return

    amount = ask_amount()
    expense = {
        "date": date.today().isoformat(),
        "category": category,
        "description": description,
        "amount": str(amount),
    }
    if save_expense(expense):
        print("Expense saved.\n")


def list_expenses():
    """Display saved expenses and their total."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses saved yet.\n")
        return

    print("\nSAVED EXPENSES")
    print("-" * 62)
    for item in expenses:
        print(
            f'{item["date"]} | {item["category"]:<12} | '
            f'{item["description"]:<22} | {Decimal(item["amount"]):>8.2f} EUR'
        )

    total = sum((Decimal(item["amount"]) for item in expenses), Decimal("0.00"))
    print("-" * 62)
    print(f"Total spending: {total:.2f} EUR\n")


def main():
    """Display the menu until the user chooses to exit."""
    while True:
        print("SIMPLE EXPENSE TRACKER")
        print("1. Add expense")
        print("2. List expenses and total")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
