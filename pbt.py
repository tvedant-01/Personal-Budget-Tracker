#  Personal Budget Tracker 
#In this project,fundamental Python concepts such as lists, loops, conditionals, and basic input/output methods are used.

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
        income = float(input("Enter income amount: ₹"))
        User_income.append(income)
        print("Income added successfully.")

    elif choice == "2":
        expense = float(input("Enter expense amount: ₹"))
        User_expense.append(expense)
        print("Expense added successfully.")

    elif choice == "3":
        total_income = sum(User_income)
        total_expense = sum(User_expense)
        balance = total_income - total_expense
        print(f"\nTotal Income: ₹{total_income}")
        print(f"Total Expenses: ₹{total_expense}")
        print(f"Current Balance: ₹{balance}")

    elif choice == "4":
        print("\nIncome History:", User_income)
        print("Expense History:", User_expense)

    elif choice == "5":
        print("Exiting Budget Tracker , Goodbye!")
        break

    else:
        print("Invalid choice\n Kindly Please select between 1 and 5.")

