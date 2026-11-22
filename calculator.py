# Personal Income Calculator

name = input("Enter your name: ")

income = float(input("Enter monthly income: "))
rent = float(input("Enter rent: "))
food = float(input("Enter food expenses: "))
transport = float(input("Enter transport expenses: "))
total_expenses = rent + food + transport
remaining_balance = income - total_expenses

# Calculate expense percentage
if income > 0:
    expense_percentage = (total_expenses / income) * 100
else:
    expense_percentage = None

# Display financial summary
print("\n------ MONTHLY FINANCIAL SUMMARY ------")
print(f"Name: {name}")
print(f"Monthly Income: KES {income:,.2f}")
print(f"Total Expenses: KES {total_expenses:,.2f}")
print(f"Remaining Balance: KES {remaining_balance:,.2f}")

if expense_percentage is not None:
    print(f"Percentage of income spent: {expense_percentage:.2f}%")
else:
    print("Expense percentage cannot be calculated.")

if remaining_balance < 0:
    print("Status: You have overspent your monthly income.")
elif remaining_balance == 0:
    print("Status: You broke even this month.")
else:
    print("Status: Great job! You stayed within your budget.")
