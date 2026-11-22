# account withdrawal program
name = input("Enter your name: ")
current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter the amount to withdraw: "))
new_balance = current_balance - withdrawal_amount

print("\n------ ACCOUNT SUMMARY ------")
print(f"Name: {name}")
print(f"Current Balance: ${current_balance:.2f}")
print(f"Withdrawal Amount: ${withdrawal_amount:.2f}")
print(f"New Balance: ${new_balance:.2f}")

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount.")
elif withdrawal_amount > float(5000):
    print("Withdrawal exceeds the daily limit.")
else:
    print("Withdrawal successful.")
