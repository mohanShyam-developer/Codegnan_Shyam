#Smart Expense Calculator
print("Welcome to Smart Expense Calculator".center(80))
print("-" * 50)

#Enter User details
name = input("Enter your name: ")

income = float(input("Enter your monthly income: "))
food = float(input("Enter food expenses: "))
travel = float(input("Enter travel expenses: "))
entertainment = float(input("Enter entertainment expenses: "))
others = float(input("Enter other expenses: "))

#Formula
total_expense = food + travel + entertainment + others
balance = income - total_expense

print("\n" + "-" * 50)
print("Name:", name)
print("Total Income:", income)
print("Total Expenses:", total_expense)
print("Remaining Balance:", balance)

print("-" * 50)

#logic
if balance > 0:
    print("Good job! You are saving money 👍")
elif balance == 0:
    print("You spent exactly your income ⚖️")
else:
    print("Warning! You are overspending ⚠️")

print("-" * 50)
