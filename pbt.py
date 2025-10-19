#  Personal Budget Tracker 
#In this project,fundamental Python concepts such as lists, loops, conditionals,exception handling and basic input/output methods are used.

print("Welcome to Personal Budget Tracker".center(50,"-"))

User_income = []
User_expense = []

while True:
    print("Choose an option of your choice :")
    print("1. Add Your Income")
    print("2. Add Your Expense")
    print("3. Show Current Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter your choice ranging between 1 to 5: ")

    if choice == "1":
        try:
            income = float(input("Enter income amount: ₹"))
            if income < 0:
                print("Income cannot be negative.")
                continue
            User_income.append(income)
            print("Income added successfully.")
        except ValueError:
            print(" Invalid input. Please enter a valid number.")


    elif choice == "2":
        try:
            expense = float(input("Enter expense amount: ₹"))
            if expense < 0:
                print("Expense cannot be negative.")
                continue
            User_expense.append(expense)
            print("Expense added successfully.")
        except ValueError:
            print(" Invalid input. Please enter a valid number.")

    elif choice == "3":
        total_income = sum(User_income)
        total_expense = sum(User_expense)
        balance = total_income - total_expense
        print("\n--- Current Financial Summary ---")
        print(f"\nTotal Income: ₹{total_income}")
        print(f"Total Expenses: ₹{total_expense}")
        print(f"Current Balance: ₹{balance}")

    elif choice == "4":
        print("\n--- Transaction History ---")
        if User_income:
            print("Income Entries:")
            for i,amount in enumerate(User_income,1):
                print(f"{i}. ₹{amount:.2f}")
        else: 
            print("No income records found")
        if User_expense:
            print("Expense Entries:")
            for i,amount in enumerate(User_expense,1):
                print(f"{i}. ₹{amount:.2f}")
        else:
            print("No expense records found.")

    elif choice == "5":
        print("Exiting Budget Tracker , Goodbye!")
        break

    else:
        print("Invalid choice\n Kindly Please select between 1 and 5.")
