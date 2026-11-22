# ==========================================================
# DIAMOND CAFE ACCOUNTING SYSTEM

# ------------------------------
# CONSTANTS
# ------------------------------

TAX_RATE = 0.05


# ------------------------------
# DATA STORAGE
# ------------------------------

# Sales records
sales_total = 0.0
tax_collected = 0.0
number_of_transactions = 0

# Expense records
expense_names = []
expense_categories = []
expense_amounts = []


# ==========================================================
# INPUT VALIDATION FUNCTIONS
# ==========================================================


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

        if answer == "y":
            return True

        elif answer == "n":
            return False

        else:
            print("Please enter y/n.")


# ==========================================================
# SALES FUNCTION
# ==========================================================


def record_sales():

    item_names = []
    quantities = []
    prices = []
    item_totals = []

    subtotal = 0.0

    print("\n========== RECORD SALES ==========")

    while True:
        # Collect product information
        item_name = get_text("Enter item name: ")

        quantity = get_positive_integer("Enter quantity sold: ")

        price = get_positive_float("Enter price per item (KES): ")

        # Calculate item total
        item_total = quantity * price

        # Store item information
        item_names.append(item_name)
        quantities.append(quantity)
        prices.append(price)
        item_totals.append(item_total)

        # Update subtotal
        subtotal += item_total

        print(f"Item total: KES {item_total:,.2f}")

        # Ask whether to add another item
        if not get_yes_no("Add another item? (yes/no): "):
            break

    # Calculate tax
    tax = subtotal * TAX_RATE

    final_total = subtotal + tax

    # Print receipt
    print("\n==============================================")
    print("                 DIAMOND CAFE RECEIPT")
    print("==============================================")

    print(f"{'Item':<15}{'Qty':>5}{'Price':>12}{'Total':>14}")
    print("----------------------------------------------")

    for i in range(len(item_names)):
        print(
            f"{item_names[i]:<15}"
            f"{quantities[i]:>5}"
            f"{prices[i]:>12,.2f}"
            f"{item_totals[i]:>14,.2f}"
        )

    print("----------------------------------------------")
    print(f"Subtotal:             KES {subtotal:,.2f}")
    print(f"Tax (5%):             KES {tax:,.2f}")
    print(f"Final Total:          KES {final_total:,.2f}")
    print("==============================================")

    return subtotal, tax


# ==========================================================
# EXPENSE FUNCTION
# ==========================================================


def record_expenses():

    print("\n========== RECORD EXPENSES ==========")

    while True:
        expense_name = get_text("Enter expense name: ")

        expense_category = get_text("Enter expense category: ")

        expense_amount = get_positive_float("Enter expense amount (KES): ")

        # Store expense information
        expense_names.append(expense_name)
        expense_categories.append(expense_category)
        expense_amounts.append(expense_amount)

        print("Expense recorded successfully!")

        if not get_yes_no("Record another expense? (yes/no): "):
            break

    # Calculate all expenses recorded so far
    total_expenses = sum(expense_amounts)

    # Display expense report
    print("\n========== EXPENSE SUMMARY ==========")

    print(f"{'Expense':<18}{'Category':<18}{'Amount (KES)':>15}")
    print("----------------------------------------------")

    for i in range(len(expense_names)):
        print(
            f"{expense_names[i]:<18}"
            f"{expense_categories[i]:<18}"
            f"{expense_amounts[i]:>15,.2f}"
        )

    print("----------------------------------------------")
    print(f"Total Expenses: KES {total_expenses:,.2f}")
    print("==============================================")

    return total_expenses


# ==========================================================
# PROFIT AND LOSS FUNCTION
# ==========================================================


def calculate_profit(sales, expenses, tax):

    net_result = sales - expenses

    print("\n========== FINANCIAL REPORT ==========")

    print(f"Sales Revenue:       KES {sales:,.2f}")
    print(f"Tax Collected:      KES {tax:,.2f}")
    print(f"Operating Expenses:  KES {expenses:,.2f}")

    print("----------------------------------")
    print(f"Simplified Result:  KES {net_result:,.2f}")

    if net_result > 0:
        print("Status: Positive operating result.")

    elif net_result < 0:
        print("Status: Negative operating result.")

    else:
        print("Status: Break-even.")

    print("==================================")

    print(
        "Note: This is a simplified calculation. "
        "Inventory costs and other accounting adjustments "
        "are not yet included."
    )


# ==========================================================
# MAIN PROGRAM
# ==========================================================

while True:
    print("\n================================")
    print("     DIAMOND CAFE ACCOUNTING SYSTEM")
    print("================================")

    print("1. Record Sales")
    print("2. Record Expenses")
    print("3. Calculate Profit/Loss")
    print("4. View Sales Summary")
    print("5. View Expense Summary")
    print("6. Exit")

    choice = input("Select an option: ").strip()

    # --------------------------------------
    # OPTION 1: RECORD SALES
    # --------------------------------------

    if choice == "1":
        subtotal, tax = record_sales()

        sales_total += subtotal
        tax_collected += tax
        number_of_transactions += 1

    # --------------------------------------
    # OPTION 2: RECORD EXPENSES
    # --------------------------------------

    elif choice == "2":
        record_expenses()

    # --------------------------------------
    # OPTION 3: CALCULATE PROFIT/LOSS
    # --------------------------------------

    elif choice == "3":
        total_expenses = sum(expense_amounts)

        calculate_profit(sales_total, total_expenses, tax_collected)

    # --------------------------------------
    # OPTION 4: VIEW SALES SUMMARY
    # --------------------------------------

    elif choice == "4":
        print("\n========== SALES SUMMARY ==========")

        print(f"Transactions: {number_of_transactions}")
        print(f"Sales Revenue: KES {sales_total:,.2f}")
        print(f"Tax Collected: KES {tax_collected:,.2f}")
        print(f"Total Including Tax: KES {sales_total + tax_collected:,.2f}")

        print("================================")

    # --------------------------------------
    # OPTION 5: VIEW EXPENSE SUMMARY
    # --------------------------------------

    elif choice == "5":
        total_expenses = sum(expense_amounts)

        print("\n========== EXPENSE SUMMARY ==========")

        for i in range(len(expense_names)):
            print(
                f"{expense_names[i]} | "
                f"{expense_categories[i]} | "
                f"KES {expense_amounts[i]:,.2f}"
            )

        print("----------------------------------")
        print(f"Total Expenses: KES {total_expenses:,.2f}")
        print("==================================")

    # --------------------------------------
    # OPTION 6: EXIT
    # --------------------------------------

    elif choice == "6":
        print("\nThank you for using Cafe Accounting System.")
        print("Program closed.")

        break

    # --------------------------------------
    # INVALID MENU OPTION
    # --------------------------------------

    else:
        print("Invalid option. Please select from 1 to 6.")
