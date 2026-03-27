
# Student Marks Manager

marks = [78, 85, 90, 67, 88]

print("Initial Marks List:")
print(marks)

# Add new mark
new_mark = int(input("Enter new mark to add: "))
marks.append(new_mark)

print("After Adding Mark:")
print(marks)

# Insert mark at position
pos = int(input("Enter position to insert mark: "))
value = int(input("Enter mark to insert: "))
marks.insert(pos, value)

print("After Inserting Mark:")
print(marks)

# Remove a mark
remove_mark = int(input("Enter mark to remove: "))
if remove_mark in marks:
    marks.remove(remove_mark)

print("After Removing Mark:")
print(marks)

# Sort marks
marks.sort()
print("Sorted Marks:")
print(marks)

# Reverse marks
marks.reverse()
print("Reversed Marks:")
print(marks)

# Display highest and lowest marks
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

print("Total Marks Count:", len(marks))































