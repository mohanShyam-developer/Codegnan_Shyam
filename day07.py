'''
student_marks=int(input(" Enter marks :"))
if student_marks>=90:
     print("you got A+ GRADE")
elif student_marks>=75:
         print(" you got A grade")
elif student_marks>=60:
             print("you got B+ grade")
else:
                 print("fail")


num_1=int(input("Enter number :"))        
num_2=int(input("Enter number :"))
'''
print("------ MOBILE RECHARGE SYSTEM ------")

choice = "yes"

while choice == "yes":

    print("\nAvailable Recharge Plans:")
    print("1. ₹199 Plan - 28 Days Validity")
    print("2. ₹399 Plan - 56 Days Validity")
    print("3. ₹599 Plan - 84 Days Validity")
    print("4. ₹999 Plan - 84 Days + Extra Data")

    plan = int(input("\nEnter plan number: "))

    # Plan selection using elif

    if plan == 1:
        amount = 199
        validity = 28

    elif plan == 2:
        amount = 399
        validity = 56

    elif plan == 3:
        amount = 599
        validity = 84

    elif plan == 4:
        amount = 999
        validity = 84

    else:
        print("Invalid plan selected!")
        continue

    # Output
    print("\n------ RECHARGE SUCCESSFUL ------")
    print("Recharge Amount: ₹", amount)
    print("Validity:", validity, "days")

    choice = input("\nDo you want another recharge? (yes/no): ")

print("\nRecharge System Closed.")















    
                
    
