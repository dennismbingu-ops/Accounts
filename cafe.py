import csv
import os
from datetime import datetime

# ==========================================
# 1. SYSTEM CONFIGURATION
# ==========================================

TAX_RATE = 0.05

SALES_FILE = "sales.csv"
EXPENSES_FILE = "expenses.csv"

# Sales information held in memory
sales_total = 0.0
tax_collected = 0.0
transaction_ids = set()

# Expense information held in memory
expense_names = []
expense_categories = []
expense_amounts = []

next_transaction_id = 1


# ==========================================
# 2. INPUT VALIDATION FUNCTIONS
# ==========================================


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter an amount greater than zero.")

        except ValueError:
            print("Invalid input. Enter a valid number.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer == "yes":
            return True

        elif answer == "no":
            return False

        else:
            print("Please enter yes or no.")


# ==========================================
# 3. CREATE CSV FILES IF THEY DO NOT EXIST
# ==========================================


def initialize_files():

    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "Transaction_ID",
                    "Date",
                    "Item",
                    "Quantity",
                    "Unit_Price",
                    "Subtotal",
                    "Transaction_Tax",
                ]
            )

    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Date", "Expense", "Category", "Amount"])


# ==========================================
# 4. LOAD PREVIOUS RECORDS
# ==========================================


def load_data():

    global sales_total
    global tax_collected
    global next_transaction_id

    # Load sales records
    with open(SALES_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transaction_id = int(row["Transaction_ID"])

            transaction_ids.add(transaction_id)

            sales_total += float(row["Subtotal"])

            tax_collected += float(row["Transaction_Tax"])

    # Determine the next transaction number
    if transaction_ids:
        next_transaction_id = max(transaction_ids) + 1

    # Load expense records
    with open(EXPENSES_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_names.append(row["Expense"])

            expense_categories.append(row["Category"])

            expense_amounts.append(float(row["Amount"]))


# ==========================================
# 5. RECORD SALES
# ==========================================


def record_sales():

    global sales_total
    global tax_collected
    global next_transaction_id

    print("\n========== RECORD SALES ==========")

    item_names = []
    quantities = []
    prices = []
    item_totals = []

    subtotal = 0.0

    while True:
        item_name = get_text("Enter item name: ")

        quantity = get_positive_integer("Enter quantity: ")

        price = get_positive_float("Enter unit price (KES): ")

        item_total = quantity * price

        item_names.append(item_name)
        quantities.append(quantity)
        prices.append(price)
        item_totals.append(item_total)

        subtotal += item_total

        print(f"Item total: KES {item_total:,.2f}")

        if not get_yes_no("Add another item? (yes/no): "):
            break

    # Calculate tax and final amount
    tax = round(subtotal * TAX_RATE, 2)

    final_total = subtotal + tax

    # Generate transaction details
    transaction_id = next_transaction_id

    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the transaction in the CSV file
    with open(SALES_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        for i in range(len(item_names)):
            # Store the transaction tax only once
            if i == 0:
                item_tax = tax
            else:
                item_tax = 0.0

            writer.writerow(
                [
                    transaction_id,
                    transaction_date,
                    item_names[i],
                    quantities[i],
                    prices[i],
                    item_totals[i],
                    item_tax,
                ]
            )

    # Update running totals
    sales_total += subtotal

    tax_collected += tax

    transaction_ids.add(transaction_id)

    next_transaction_id += 1

    # Print receipt
    print("\n========== CUSTOMER RECEIPT ==========")

    print(f"Transaction Number: {transaction_id}")

    print(f"Date: {transaction_date}")

    print("--------------------------------------")

    print(f"{'Item':<15}{'Qty':<6}{'Price':<12}{'Total':<12}")

    print("--------------------------------------")

    for i in range(len(item_names)):
        print(
            f"{item_names[i]:<15}"
            f"{quantities[i]:<6}"
            f"{prices[i]:<12.2f}"
            f"{item_totals[i]:<12.2f}"
        )

    print("--------------------------------------")

    print(f"Subtotal: KES {subtotal:,.2f}")

    print(f"Tax (5%): KES {tax:,.2f}")

    print(f"FINAL TOTAL: KES {final_total:,.2f}")

    print("======================================")

    print("Sales record saved successfully!")


# ==========================================
# 6. RECORD BUSINESS EXPENSES
# ==========================================


def record_expenses():

    print("\n========== RECORD EXPENSES ==========")

    while True:
        expense_name = get_text("Enter expense name: ")

        category = get_text("Enter expense category: ")

        amount = get_positive_float("Enter expense amount (KES): ")

        expense_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save expense in CSV file
        with open(EXPENSES_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([expense_date, expense_name, category, amount])

        # Update in-memory records
        expense_names.append(expense_name)

        expense_categories.append(category)

        expense_amounts.append(amount)

        print("\nExpense saved successfully!")

        if not get_yes_no("Record another expense? (yes/no): "):
            break

    total_expenses = sum(expense_amounts)

    print(f"\nTotal recorded expenses: KES {total_expenses:,.2f}")


# ==========================================
# 7. CALCULATE PROFIT OR LOSS
# ==========================================


def calculate_profit():

    total_expenses = sum(expense_amounts)

    simplified_result = sales_total - total_expenses

    print("\n========== PROFIT / LOSS REPORT ==========")

    print(f"Sales Revenue: KES {sales_total:,.2f}")

    print(f"Tax Collected: KES {tax_collected:,.2f}")

    print(f"Total Expenses: KES {total_expenses:,.2f}")

    print("------------------------------------------")

    print(f"Simplified Operating Result: KES {simplified_result:,.2f}")

    if simplified_result > 0:
        print("Result: SURPLUS")

    elif simplified_result < 0:
        print("Result: DEFICIT")

    else:
        print("Result: BREAK-EVEN")

    print("==========================================")


# ==========================================
# 8. VIEW SALES SUMMARY
# ==========================================


def view_sales_summary():

    print("\n========== SALES SUMMARY ==========")

    print(f"Number of Transactions: {len(transaction_ids)}")

    print(f"Total Sales Revenue: KES {sales_total:,.2f}")

    print(f"Tax Collected: KES {tax_collected:,.2f}")

    print(f"Total Including Tax: KES {sales_total + tax_collected:,.2f}")

    print("===================================")


# ==========================================
# 9. VIEW EXPENSE SUMMARY
# ==========================================


def view_expense_summary():

    print("\n========== EXPENSE SUMMARY ==========")

    if not expense_names:
        print("No expenses have been recorded.")

    else:
        print(f"{'Expense':<18}{'Category':<18}{'Amount (KES)':<15}")

        print("-----------------------------------------------")

        for i in range(len(expense_names)):
            print(
                f"{expense_names[i]:<18}"
                f"{expense_categories[i]:<18}"
                f"{expense_amounts[i]:<15,.2f}"
            )

    total_expenses = sum(expense_amounts)

    print("-----------------------------------------------")

    print(f"Total Expenses: KES {total_expenses:,.2f}")

    print("===================================")


# ==========================================
# 10. MAIN MENU
# ==========================================


def main():

    # Prepare files and load existing records
    initialize_files()

    load_data()

    print("\n====================================")
    print("       CAFE ACCOUNTING SYSTEM")
    print("====================================")

    print("Previous records loaded successfully!")

    while True:
        print("\n========== MAIN MENU ==========")

        print("1. Record Sales")

        print("2. Record Expenses")

        print("3. Calculate Profit / Loss")

        print("4. View Sales Summary")

        print("5. View Expense Summary")

        print("6. Exit")

        print("===============================")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            record_sales()

        elif choice == "2":
            record_expenses()

        elif choice == "3":
            calculate_profit()

        elif choice == "4":
            view_sales_summary()

        elif choice == "5":
            view_expense_summary()

        elif choice == "6":
            print("\nThank you for using the Café Accounting System!")

            print("All records have been saved.")

            break

        else:
            print("Invalid selection. Please choose between 1 and 6.")


# ==========================================
# 11. START THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
