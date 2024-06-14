import sys
import os

# Add the current directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.user import User
from lib.expense import Expense
from lib.income import Income
from lib.savingsgoal import SavingsGoal

def main():
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add User")
        print("2. Delete User")
        print("3. Add Expense")
        print("4. List Expenses")
        print("5. Add Income")
        print("6. List Income")
        print("7. Add Savings Goal")
        print("8. List Savings Goals")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            # User.create(username, password, email)
            user = User(username=username, password=password, email=email)
            user.save()
            print("User created successfully")
            # print(f"User {username} added.")

        elif choice == '2':
            user_id = input("Enter user ID to delete: ")
            user = User.delete(user_id)
            # if user:
            print("User deleted successfully.")
            # else:
                # print("User not found.")      
        
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            date = input("Enter expense date (YYYY-MM-DD): ")
            Expense.create(description, amount, date, user_id)
            print(f"Expense '{description}' added.")

        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            expenses = Expense.get_all(user_id)
            if expenses:
                for expense in expenses:
                    print(f"{expense[0]} | {expense[1]} | {expense[2]} | {expense[3]} | {expense[4]}")
            else:
                print("No expenses found.")
        
        elif choice == '5':
            user_id = int(input("Enter user ID: "))
            source = input("Enter income source: ")
            amount = float(input("Enter income amount: "))
            date = input("Enter income date (YYYY-MM-DD): ")
            Income.create(source, amount, date, user_id)
            print(f"Income '{source}' added.")

        elif choice == '6':
            user_id = int(input("Enter user ID: "))
            income = Income.get_all(user_id)
            if income:
                for inc in income:
                    print(f"{inc[0]} | {inc[1]} | {inc[2]} | {inc[3]} | {inc[4]}")
            else:
                print("No income found.")
        
        elif choice == '7':
            user_id = int(input("Enter user ID: "))
            goal_name = input("Enter goal name: ")
            target_amount = float(input("Enter target_amount: "))
            SavingsGoal.create(goal_name, target_amount, user_id)
            print(f"Savings goal '{goal_name}' added.")

        elif choice == '8':
            user_id = int(input("Enter user ID: "))
            goals = SavingsGoal.get_all(user_id)
            if goals:
                for goal in goals:
                    print(f"{goal[0]} | {goal[1]} | {goal[2]} | {goal[3]} | {goal[4]}")
            else:
                print("No savings goals found.")
        
        elif choice == '9':
            print("Exiting the Personal Finance Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
