# Expense Tracker
# By Pukar Budhathoki

import json
import datetime

def add_expense(expenses, amount, category, description):
    expense = {
        "date": str(datetime.date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print(f"✓ Expense added: {category} — ${amount}")
    return expenses

def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    total = 0
    categories = {}
    
    print("\n================================")
    print("       EXPENSE SUMMARY")
    print("================================")
    
    for expense in expenses:
        total += expense["amount"]
        cat = expense["category"]
        if cat in categories:
            categories[cat] += expense["amount"]
        else:
            categories[cat] = expense["amount"]
        
        print(f"{expense['date']} | {expense['category']} | ${expense['amount']} | {expense['description']}")
    
    print("\n--- By Category ---")
    for cat, amount in categories.items():
        print(f"{cat}: ${amount}")
    
    print(f"\nTotal Spent: ${total}")
    print("================================")

def save_expenses(expenses):
    with open("/Users/mac/Desktop/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    print("Expenses saved to Desktop.")

def main():
    expenses = []
    
    print("================================")
    print("       EXPENSE TRACKER")
    print("   By Pukar Budhathoki")
    print("================================\n")
    
    while True:
        print("\nWhat do you want to do?")
        print("1 - Add expense")
        print("2 - View summary")
        print("3 - Save and exit")
        
        choice = input("\nEnter 1, 2 or 3: ")
        
        if choice == "1":
            amount = float(input("Amount ($): "))
            category = input("Category (Food/Transport/Learning/Other): ")
            description = input("Description: ")
            expenses = add_expense(expenses, amount, category, description)
            
        elif choice == "2":
            show_summary(expenses)
            
        elif choice == "3":
            save_expenses(expenses)
            print("Goodbye. Keep tracking. 💪")
            break
        
        else:
            print("Invalid choice. Try again.")

main()