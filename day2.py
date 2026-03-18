'''
variables-->varaiables are named storage location that is used to hold data in the memory,
to make it simple. It is the the label which points
out to a value --> storage placeholders

Rules for defining variables
-->A-Z,a-z,0-9.
-->start with uppercase,lowercase letters,even with a underscore.
-->but you cannot start with symbols (@,#,$...), and numbers also.

the better preferable way is go with general purpose--> you want to store
your deatils name,email_id,account_number...

'''
'''
a=1
b=5

#python is dynamically typed,you need not define the datatype and also
#only the recent value to the varaible with same name is pointed

print(a)
print(b)

#1a23 =25 #syntax error
#@werf =4.5 #syntax error
#$sdsf =12 #invalid syntax
#store your personal details

name ="codegnan"
location="visakhapatnam"
age=7
email_id="codegnan@gmail.com"
print(name ,location ,age , email_id)

#how to assign multiple values to a variable
shyam,raju,kartheek=21,10,23
print(shyam)
print(raju)
print(kartheek)

#assign same values to multiple variables

x=y=z=21
print(x,y,z)

#keyboards are reserved words will have specific usage
#there are 35 keywords in python
#never use keyboards as identifiers

#if =23
#lamda='shyam'
#false=0 # cannot assign
#python is case-senstive

false =25

#identifiers are names given to variables,functions,classes,objects.....

#literals are fixed values to a identifier
age=25
name='shyam'

#single line comments--> #
# mutliple line comments-->''''start....end ''''''

#name is identifier,25 is literal
#built-in datatypes -->numeric,boolean,collections

#Numeric datatypes-->int,float,comples
#int--> count,values,quantities
#float-->temperature,percentage,price
#complex-->specific conversions(real and imaginary)

count=40
print(count)
print(type(count))
price =175.5
print(type(price))

value =2+3j
print(value)
print(type(value))
#typecasting-->converting one type to another

#int-->float,complex

age=25
print(type(age))
b=float(age)
print(type(b))'''

'''
age=21
print(type(age))

y=complex(age)      #converting int to complex
print(type(y))
print(y)

height=5.9
print(type(height))

z=complex(height)  #converting float to complex
print(type(z))
print(z)

x=5+3j
print(type(x))

p=float(x)
print(type(p))  #cannot be done
print(p)
'''
'''
#boolean datatype-->validation -->true or false

a=True
print(a)


#typeconversion of bool

b=int(a)
print(b)

c=float(a)
print(c)

d=complex(float(int(False)))
print(d)
print(type(d))'''


#input -->input()
#output -->print()
'''
a=5
print(a)

a=int(input("enter a number 1:"))  #if i didnt place int before input then the type will result as string
print(a)
print(type(a))'''

'''
x=int(input("enter a number 1:"))
print(x)
print(type(x))

y=int(input("enter a number 2:"))
print(y)
print(type(y))

result=x*y
print(result)'''

#details of the student


college="Welcome to Codegnan"
print(college.center(140))

name=(input("Enter Student name:"))
admission_fees = int(input("Enter Admission fees:"))
tuition_fees = float(input("Enter Tuition fees:"))
hostel_fees = float(input("Enter Hostel fees:"))
total_fees =admission_fees + tuition_fees + hostel_fees
print("----------------------------")
print("Student name:",name)
print("Admission fees:",admission_fees)
print("Tuition fees:",tuition_fees)
print("Hostel fees:",hostel_fees)
print("Total fees:",total_fees)
print("----------------------------")'''



































































