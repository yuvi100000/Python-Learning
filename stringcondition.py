# ============================================
# PYTHON CONDITIONAL STATEMENTS
# Author : Banti Singh
# ============================================
# --------------------------------------------
# 1. Boolean Values
# --------------------------------------------
print(True)
print(False)
print(10 > 5)      # True
print(10 < 5)      # False
# --------------------------------------------
# 2. Comparison Operators
# --------------------------------------------
a = 20
b = 10
print(a == b)      # Equal
print(a != b)      # Not Equal
print(a > b)       # Greater Than
print(a < b)       # Less Than
print(a >= b)      # Greater Than Equal
print(a <= b)      # Less Than Equal
# --------------------------------------------
# 3. if Statement
# --------------------------------------------
age = 20
if age >= 18:
    print("Eligible for Voting")
# --------------------------------------------
# 4. if-else Statement
# --------------------------------------------
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")
# --------------------------------------------
# 5. if-elif-else Statement
# --------------------------------------------
marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 33:
    print("Pass")
else:
    print("Fail")
# --------------------------------------------
# 6. Nested if
# --------------------------------------------
age = 22
license = True
if age >= 18:
    if license:
        print("You Can Drive")
# --------------------------------------------
# 7. Multiple if
# --------------------------------------------
marks = 90
if marks >= 33:
    print("Pass")
if marks >= 75:
    print("Distinction")
# --------------------------------------------
# 8. Logical Operators
# --------------------------------------------
# AND
age = 20
license = True
if age >= 18 and license:
    print("Drive")
# OR
marks = 30
sports = True
if marks >= 33 or sports:
    print("Selected")
# NOT
rain = False
if not rain:
    print("Go Outside")
# --------------------------------------------
# 9. Voting Program
# --------------------------------------------
age = 21
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
# --------------------------------------------
# 10. Even Odd Program
# --------------------------------------------
number = 25
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
# --------------------------------------------
# 11. Positive Negative Zero
# --------------------------------------------
num = -10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# --------------------------------------------
# 12. Greatest of Two Numbers
# --------------------------------------------
a = 50
b = 80
if a > b:
    print("A is Greater")
else:
    print("B is Greater")
# --------------------------------------------
# 13. Login System
# --------------------------------------------
username = "admin"
password = "python123"
if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")
# --------------------------------------------
# 14. ATM Program
# --------------------------------------------
pin = 1234
balance = 12000
if pin == 1234:
    if balance >= 5000:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
# --------------------------------------------
# 15. Movie Ticket Program
# --------------------------------------------
age = 15
ticket = True
if age >= 12:
    if ticket:
        print("Enjoy Movie")
    else:
        print("Buy Ticket")
else:
    print("Entry Denied")
# --------------------------------------------
# END OF CONDITIONAL STATEMENTS
# --------------------------------------------