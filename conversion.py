# ============================================
# Topic      : Python Type Conversion
# Author     : Yuvraj
# Description: Examples of Implicit and Explicit Type Conversion
# ============================================

# --------------------------------------------
# 1. Implicit Type Conversion
# --------------------------------------------

a = 1          # Integer
b = 2.0        # Float

# Python automatically converts int to float
c = a + b

print("Result:", c)
print("Data Type:", type(c))

# Output:
# Result: 3.0
# Data Type: <class 'float'>


# --------------------------------------------
# 2. Explicit Type Conversion
# --------------------------------------------

# String to Float
n = float("19")

print("Value of n:", n)
print("Data Type:", type(n))

# Float to Integer
m = int(1.2)

print("Value of m:", m)
print("Data Type:", type(m))

# Integer
o = 2

print("o + m =", o + m)
print("Data Type:", type(o + m))

# Output:
# Value of n: 19.0
# Data Type: <class 'float'>
#
# Value of m: 1
# Data Type: <class 'int'>
#
# o + m = 3
# Data Type: <class 'int'>