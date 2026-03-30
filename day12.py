##a=9
##print(a)
##for j in range(1,10):
##    print(j)

##range()--->this is used to generate number
##syntax()--->range(start,end,step)


##for i in range(2,30,2):
##    print(i)

##an=[1,2,3]
##vs=str(an)
##print(type(vs))
##print(vs)
##print(tuple(an))

##reverse_str="mohanshyam"
##print(reverse_str[::-1])

##user_input=input("enter a number:")
##empty=""
##for i in range(2,20,2):
##    print(f"{i} is even number")
##    
##for j in range(1,20,2):
##    print(f"{j} is odd number")

##for num in range(1,100):
##    if num %2==0:
##        print(f"{num} is even number")
##    else:
##        print(f"{num} is odd number")


numbers = []

n = int(input("How many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

unique_numbers = set(numbers)

print("\nEven numbers:", even_count)
print("Odd numbers:", odd_count)
print("Unique numbers:", unique_numbers)


























