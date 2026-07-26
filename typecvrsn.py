# type conversion
a = 1
b = 2.0
c = a + b
print(c) # output is 3.0 because of type conversion 
print(type(c)) # output is <class 'float'> because of type conversion 
n = float("19") 
m = 1.2
print(type(n+m)) 
# input function 
name = input("Enter your name:") 
print("welcome",name) 
#  if we  input a number it will be treated as a string 
age = input("enter your age:") 
print(type("Your age is",age))   
first = int(input("enter first number:"))   # input function always returns a string 
second = int(input("enter second number:"))
print("the sum is",first + second) 