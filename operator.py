# ==========================================================
# Topic       : Python Operators
# Author      : Yuvraj
# Description : This program demonstrates different types of
#               operators in Python with examples.
# ==========================================================


# ----------------------------------------------------------
# 1. Arithmetic Operators
# ----------------------------------------------------------
# Arithmetic operators are used to perform mathematical
# operations on numbers.

num1 = 5
num2 = 2

addition = num1 + num2
print("Addition:", addition)

subtraction = num1 - num2
print("Subtraction:", subtraction)

multiplication = num1 * num2
print("Multiplication:", multiplication)

division = num1 / num2
print("Division:", division)

modulus = num1 % num2
print("Modulus:", modulus)

exponent = num1 ** num2
print("Exponent (Power):", exponent)


# ----------------------------------------------------------
# 2. Relational (Comparison) Operators
# ----------------------------------------------------------
# These operators compare two values and return
# either True or False.

print("Equal to:", num1 == num2)
print("Not Equal to:", num1 != num2)
print("Greater Than:", num1 > num2)
print("Less Than:", num1 < num2)
print("Greater Than or Equal To:", num1 >= num2)
print("Less Than or Equal To:", num1 <= num2)


# ----------------------------------------------------------
# 3. Assignment Operators
# ----------------------------------------------------------
# Assignment operators are used to assign or update values.

value = 10

value += 10      # value = value + 10
print("After += :", value)

value -= 5       # value = value - 5
print("After -= :", value)

value *= 2       # value = value * 2
print("After *= :", value)

value /= 3       # value = value / 3
print("After /= :", value)

value %= 4       # value = value % 4
print("After %= :", value)

value **= 2      # value = value ** 2
print("After **= :", value)


# ----------------------------------------------------------
# 4. Logical Operators
# ----------------------------------------------------------
# Logical operators are used to combine conditions.

x = True
y = False

print("AND Operator :", x and y)
print("OR Operator  :", x or y)
print("NOT x        :", not x)
print("NOT y        :", not y)