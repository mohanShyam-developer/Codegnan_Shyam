# Realistic ATM Machine System (ATM Cash Hidden)

print("------ ATM MACHINE ------")

# ATM machine cash (hidden from user)
atm_cash = 100000   # 1 lakh inside ATM

# User account details
correct_pin = 1234
user_balance = 60000   # User account balance

minimum_balance = 1000
daily_withdraw_limit = 25000

# PIN attempts
attempts = 0

while attempts < 3:

    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:

        print("\nAccess Granted")

        print("\nSelect Transaction:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        # Check Balance
        if choice == 1:
            print("Your Account Balance:", user_balance)

        # Withdraw Money
        elif choice == 2:

            withdraw_amount = int(input("Enter amount to withdraw: "))

            if withdraw_amount <= 0:
                print("Enter valid amount")

            elif withdraw_amount > daily_withdraw_limit:
                print("Withdrawal exceeds daily limit")

            elif withdraw_amount > user_balance:
                print("Insufficient account balance")

            elif withdraw_amount > atm_cash:
                print("Unable to process transaction. Please try another ATM.")

            elif user_balance - withdraw_amount < minimum_balance:
                print("Minimum balance of ₹1000 must be maintained")

            else:
                user_balance -= withdraw_amount
                atm_cash -= withdraw_amount

                print("Withdrawal Successful")
                print("Remaining Account Balance:", user_balance)
                print("Thank you for using ATM")

        # Deposit Money
        elif choice == 3:

            deposit_amount = int(input("Enter amount to deposit: "))

            if deposit_amount <= 0:
                print("Enter valid deposit amount")

            else:
                user_balance += deposit_amount
                atm_cash += deposit_amount

                print("Deposit Successful")
                print("Updated Account Balance:", user_balance)

        # Exit
        elif choice == 4:
            print("Thank you for using ATM")

        else:
            print("Invalid Choice")

        break

    else:
        attempts += 1
        print("Wrong PIN")

        if attempts == 3:
            print("Card Blocked due to 3 wrong attempts")
