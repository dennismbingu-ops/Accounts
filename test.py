balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount.")

elif withdrawal > balance:
    print("Insufficient balance.")

else:
    remaining_balance = balance - withdrawal

    print("Transaction approved.")
    print(f"Remaining balance: KES {remaining_balance:,.2f}")

print("welcome back to the bank")
