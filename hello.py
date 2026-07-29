# ==========================================================
# Python Basics
# Author      : Yuvraj
# Description : Variables, Data Types, Operators,
#               Type Conversion, Input, Strings,
#               and Conditional Statements
# ==========================================================


# ----------------------------------------------------------
# 1. Variables
# ----------------------------------------------------------

name = "Banti"
print(name)

# 'name' is a variable and "Banti" is the value stored in it.

age = 23
print(age)


# ----------------------------------------------------------
# 2. Data Types
# ----------------------------------------------------------

price = 120.00

print(type(name))
print(type(age))
print(type(price))

print("My name is", name)


# ----------------------------------------------------------
# 3. Arithmetic Operators
# ----------------------------------------------------------

a = 3
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# ----------------------------------------------------------
# 4. Relational Operators
# ----------------------------------------------------------

a = 10
b = 20

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a < b)    # Less than
print(a > b)    # Greater than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to


# ----------------------------------------------------------
# 5. Logical Operators
# ----------------------------------------------------------

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# ----------------------------------------------------------
# 6. Type Conversion
# ----------------------------------------------------------

m = 1
j = 2.5

print(m + j)          # int + float = float

l = 10

print(j + l)


# ----------------------------------------------------------
# 7. User Input
# ----------------------------------------------------------

roll_no = input("Enter your roll number: ")
print("Roll Number:", roll_no)

email_id = int(input("Enter your Email ID Number: "))
print(type(email_id))

phone_number = float(input("Enter your Phone Number: "))
print(type(phone_number))

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Sum:", num1 + num2)


# ----------------------------------------------------------
# 8. String Functions
# ----------------------------------------------------------

text = "I am student"

print(text.endswith("ent"))
print(text.endswith("i"))
print(text.startswith("I"))
print(text.startswith("am"))

print(text.capitalize())

print(text.replace("student", "Python Developer"))

print(text.find("m"))

print(text.count("i"))


# ----------------------------------------------------------
# 9. Conditional Statements
# ----------------------------------------------------------

my_age = 23

if my_age >= 18:
    print("Eligible for Voting")

if my_age <= 19:
    print("You are a teenager.")