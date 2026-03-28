# Python Day 11 
# Duplicate Mobile Number Remover System

mobile_numbers = []

n = int(input("Enter how many mobile numbers: "))

for i in range(n):
    number = input("Enter mobile number: ")
    mobile_numbers.append(number)

print("\nAll Mobile Numbers:")
for num in mobile_numbers:
    print(num)

# Remove duplicates using set
unique_numbers = set(mobile_numbers)

print("\nUnique Mobile Numbers:")
for num in unique_numbers:
    print(num)

print("\nTotal Numbers Entered:", len(mobile_numbers))
print("Unique Numbers Count:", len(unique_numbers))
