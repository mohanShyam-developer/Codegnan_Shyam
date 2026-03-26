#Day-10— Tuple Operations Program
'''
What is a Tuple in Python?
A tuple is a collection of items stored in a single variable.
It is similar to a list, but the main difference is:
Tuple is immutable, which means its values cannot be changed after creation.
Tuples are written using round brackets ( )
'''
# 1. Creating Tuple
student = ("Mohan", 20, "Bangalore", "Python")

print("Original Tuple:")
print(student)

# 2. Accessing Elements
print("\nAccessing Elements:")
print("Name:", student[0])
print("Age:", student[1])

# 3. Slicing Tuple
print("\nSlicing Tuple:")
print("First two elements:", student[0:2])

# 4. Tuple Length
print("\nLength of Tuple:")
print(len(student))

# 5. Looping Through Tuple
print("\nLooping through Tuple:")
for item in student:
    print(item)

# 6. Membership Check
print("\nMembership Check:")
print("Mohan" in student)

# 7. Tuple Concatenation
new_data = ("India",)
student = student + new_data

print("\nAfter Concatenation:")
print(student)

# 8. Tuple Repetition
print("\nTuple Repetition:")
numbers = (1, 2, 3)
print(numbers * 3)

# 9. Updating Tuple 
student_list = list(student)

student_list[1] = 21   

student = tuple(student_list)

print("\nAfter Updating Tuple:")
print(student)

# 10. Built-in Functions
numbers = (10, 20, 30, 40, 20)

print("\nBuilt-in Functions:")
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# count()
print("Count of 20:", numbers.count(20))

# index()
print("Index of 30:", numbers.index(30))
