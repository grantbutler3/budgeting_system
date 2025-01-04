import json
import os

class BudgetingSystem:
    def __init__(self, filename='budget.json'):
        self.filename = filename
        self.budget_data = self.load_budget_data()

    def load_budget_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {'income': 0, 'expenses': [], 'savings': 0}

    def save_budget_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.budget_data, file, indent=4)

    def add_income(self, amount):
        self.budget_data['income'] += amount
        self.save_budget_data()
        print(f"Added income: ${amount:.2f}")

    def add_expense(self, description, amount):
        self.budget_data['expenses'].append({'description': description, 'amount': amount})
        self.save_budget_data()
        print(f"Added expense: {description} - ${amount:.2f}")

    def calculate_savings(self):
        total_expenses = sum(expense['amount'] for expense in self.budget_data['expenses'])
        self.budget_data['savings'] = self.budget_data['income'] - total_expenses
        self.save_budget_data()
        return self.budget_data['savings']

    def display_budget(self):
        print("\n--- Budget Summary ---")
        print(f"Total Income: ${self.budget_data['income']:.2f}")
        print("Expenses:")
        for expense in self.budget_data['expenses']:
            print(f"  {expense['description']}: ${expense['amount']:.2f}")
        print(f"Total Savings: ${self.calculate_savings():.2f}")
        print("----------------------\n")

def main():
    budgeting_system = BudgetingSystem()

    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Budget")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            budgeting_system.add_income(amount)
        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            budgeting_system.add_expense(description, amount)
        elif choice == '3':
            budgeting_system.display_budget()
        elif choice == '4':
            print("Exiting the budgeting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()