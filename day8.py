''' strings-- this is a sequence of charecters /collection of charecters , which represented by double quotes(" ") or single('  ') quotes
and  we can acess using indexing '''
'''
What is Indexing?
Indexing means accessing characters using position numbers.
Python index starts from 0
Negative indexing starts from -1 (last character)
# Indexing Example

sentence = "im mohan shyam and im from codegnan"

# Positive Indexing
print("First character:", sentence[0])
print("Second character:", sentence[1])

# Negative Indexing
print("Last character:", sentence[-1])
print("Second last character:", sentence[-2])

# Slicing
print("First 5 characters:", sentence[0:5])
print("From index 3 to 10:", sentence[3:10])

# Reverse string
print("Reversed sentence:", sentence[::-1])
'''
'''S
any="python programming"
print(any[2]) #TypeError: string indices must be integers, not 'tuple'-[2,3,4]
#slicing-
print(any[7:12])
print(any[0:14])
print(any[3:17])
print(any[4:9])
print(any.replace("python","java"))'''


##statement = "im mohan shyam and im from codegnan"
##
##print("First character:", statement[0])
##
##print("Last character:", statement[-1])
##
##print("First word:", statement[0:2])
##
##print("Second word:", statement[3:8])
##
##print("Third word:", statement[9:14])
##
##print("Part of sentence:", statement[19:26])
##
##print("Last word:", statement[-8:])
##
##print("Every 2nd character:", statement[::2])
##
##print("Reversed statement:", statement[::-1])
### Original statement
##statement = "im mohan shyam and im from codegnan"
##
##print("Original Statement:")
##print(statement)
##
### 1.Convert to uppercase
##print("\nUppercase:")
##print(statement.upper())
##
### 2.Convert to lowercase
##print("\nLowercase:")
##print(statement.lower())
##
### 3.Split words using split()
##print("\nSplit into words:")
##words = statement.split()
##print(words)
##
### 4.Print each word using split()
##print("\nPrinting each word separately:")
##for word in words:
##    print(word)
##
### 5.Replace a word
##print("\nReplace 'codegnan' with 'python':")
##print(statement.replace("codegnan", "python"))
##
### 6.Count number of words
##print("\nNumber of words:")
##print(len(words))
##
### 7.Find position of a word
##print("\nPosition of 'shyam':")
##print(statement.find("shyam"))
##
### 8.Check if sentence starts with 'im'
##print("\nStarts with 'im'?")
##print(statement.startswith("im"))
##
### 9.Check if sentence ends with 'codegnan'
##print("\nEnds with 'codegnan'?")
##print(statement.endswith("codegnan")



#User Registration Formatter

name = input("Enter your full name: ").strip()
email = input("Enter your email: ").strip()

print("\n----- USER DETAILS -----")

# Format name
formatted_name = name.title()
print("Formatted Name:", formatted_name)

# Create username
username = name.lower().replace(" ", "_")
print("Generated Username:", username)

# Email analysis
at_pos = email.find("@")

if at_pos != -1:
    
    email_name = email[:at_pos]
    domain = email[at_pos+1:]

    print("Email Username:", email_name)
    print("Email Domain:", domain)

else:
    print("Invalid Email")

# Name details
words = name.split()

print("First Name:", words[0])
print("Last Name:", words[-1])

# Initials
print("Initials:", words[0][0], words[-1][0])

# Length check
print("Total Name Characters:", len(name.replace(" ", "")))























