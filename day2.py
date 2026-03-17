
#user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- User Details ---")
print("Hello,", name + "!")
print("You are", age, "years old.")

#logic
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
