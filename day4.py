

# Input: Subject names
subjects = input("Enter subject names separated by commas: ").split(',')

# Input: Marks for each subject
marks_list = []
for subject in subjects:
    marks = int(input(f"Enter marks for {subject.strip()} out of 100: "))
    marks_list.append(marks)

# Calculate total and average
total_marks = sum(marks_list)
average = total_marks / len(marks_list)

# Determine grade based on average
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

#pass/fail
status = "Pass ✅" if average >= 50 else "Fail ❌"

# Display results
print("\n----- Result Summary -----")
print(f"Subjects: {', '.join(subjects)}")
print(f"Marks: {marks_list}")
print(f"Total Marks: {total_marks} / {len(subjects)*100}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")
