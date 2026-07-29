# ==========================================================
# Topic       : Python Input Function
# Author      : Yuvraj
# Description : This program demonstrates how to take user
#               input using the input() function and check
#               the data type of each input.
# ==========================================================

# ----------------------------------------------------------
# 1. Taking User's Name
# ----------------------------------------------------------

name = input("Enter your name: ")

print("Name:", name)
print("Data Type:", type(name))


# ----------------------------------------------------------
# 2. Taking User's Roll Number
# ----------------------------------------------------------

roll_number = input("Enter your roll number: ")

print("Roll Number:", roll_number)
print("Data Type:", type(roll_number))


# ----------------------------------------------------------
# 3. Taking User's Email ID
# ----------------------------------------------------------

email = input("Enter your Email ID: ")

print("Email:", email)
print("Data Type:", type(email))


# ----------------------------------------------------------
# Note:
# The input() function always returns data in string format.
# To convert input into int or float, use int() or float().
# ----------------------------------------------------------