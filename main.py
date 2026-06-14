import os

import db

from helpers import get_amount, get_category, get_note, press_enter_to_continue

def main():
    while True:
        os.system("cls")

        print("=" * 40)
        print("Spending Snapshot")
        print("=" * 40)

        print("1. Add Expense")
        print("2. Set Budget")
        print("3. List Expenses")
        print("4. Show Summary")
        print("0. Exit")

        choice = input("\n> ")
        if choice == '0': break

        match choice:
            case "1": add_expense()
            case "2": set_budget()
            case "3": list_expenses()
            case "4": show_summary()
                

def add_expense():
    category = get_category()
    amount = get_amount()
    note = get_note()

    db.add_expense(category, amount, note)
    print(f"Expense for ${amount:,.2f} add to '{category}'.")

    press_enter_to_continue()

def set_budget():
    category = get_category()
    amount = get_amount()

    db.set_budget(category, amount)
    print(f"Budget set at ${amount:,.2f} for '{category}'.")

    press_enter_to_continue()

def list_expenses():
    expenses = db.get_expenses()

    print("\n===== Expense List =====")
    
    if not expenses:
        print("No expenses to display.")
        return

    for exp in expenses:
            print("Category:", exp[0])
            print("Amount: $", exp[1])
            print("Note:", exp[2])
            print("Date:", exp[3])
    
    press_enter_to_continue()

def show_summary():
    summary = db.get_summary()

    print("\n===== Category Summary =====")
    
    if not summary:
        print("No expenses to display.")
        return

    for item in summary:
        print(f"Total spent in {item[0]}: ${item[1]:,.2f}")

    press_enter_to_continue()

if __name__ == "__main__":
    db.init_db()
    main()