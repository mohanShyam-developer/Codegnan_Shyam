# Count vowels in a string

##text = input("Enter a word: ")
##count = 0
##for i in text:
##    if i.lower() in "aeiou":
##        count += 1
##print("Number of vowels:", count)

## Reverse string without using reverse()

##text = input("Enter a word: ")
##reverse = ""
##for i in text:
##    reverse = i + reverse
##print("Reversed string:", reverse)
##

## Check palindrome using for loop

text = input("Enter a word: ")
reverse = ""
for i in text:
    reverse = i + reverse   
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
