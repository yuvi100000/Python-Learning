# ==========================
# PYTHON STRINGS
# ==========================

print("Hello Banti")
print("MASTER OF PYTHON")

# Variables
name = "yuvraj"
age = "23"

# ==========================
# Type
# ==========================
print(type(name))
print(type(age))

# ==========================
# String Concatenation (+)
# ==========================
first_name = "Yuvraj"
last_name = "Singh"

print(first_name + " " + last_name)

# ==========================
# String Repetition (*)
# ==========================
print("Hi " * 3)

# ==========================
# Length
# ==========================
print(len(name))

# ==========================
# Indexing
# ==========================
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Negative Indexing
print(name[-1])
print(name[-2])
print(name[-3])

# ==========================
# Slicing
# ==========================
print(name[0:5])
print(name[:])
print(name[2:])
print(name[:4])
print(name[1:5])
print(name[-4:])
print(name[::-1])      # Reverse String
print(name[::2])       # Every 2nd character

# ==========================
# Membership Operators
# ==========================
print("yu" in name)
print("abc" in name)
print("abc" not in name)

# ==========================
# Comparison Operators
# ==========================
print(name == "yuvraj")
print(name != "python")
print(name > "apple")

# ==========================
# String Methods
# ==========================
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())

# ==========================
# Find & Count
# ==========================
print(name.find("v"))
print(name.find("z"))
print(name.count("a"))
print(name.count("y"))

# ==========================
# Replace
# ==========================
print(name.replace("y", "Y"))
print(name.replace("raj", "RAJ"))

# ==========================
# Startswith & Endswith
# ==========================
print(name.startswith("yu"))
print(name.endswith("raj"))

# ==========================
# Strip
# ==========================
text = "   Python Programming   "

print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# ==========================
# Split & Join
# ==========================
sentence = "I Love Python"

words = sentence.split()
print(words)

print("-".join(words))
print("*".join(words))

# ==========================
# Checking Methods
# ==========================
print("PYTHON".isupper())
print("python".islower())
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("Python".isidentifier())

# ==========================
# Escape Characters
# ==========================
print("Hello\nBanti")
print("Hello\tBanti")
print("He said \"Hello\"")

# ==========================
# String Formatting
# ==========================
print("My name is " + name)

print(f"My name is {name}")
print(f"My age is {age}")

print("My name is {} and my age is {}".format(name, age))

# ==========================
# String Multiplication
# ==========================
print("=" * 40)
print("*" * 20)

# ==========================
# Reverse String
# ==========================
print(name[::-1])

# ==========================
# Program End
# ==========================
print("All String Operations Completed Successfully!")