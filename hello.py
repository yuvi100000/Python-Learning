name="banti"
print(name)
# name is variable and "banti" is value assigned to the variable name.
age = 23
print(age)
""" data type  """
PRICE = 120.00 #floatdatatype
print(type(name))
print(type(age))
print(type(PRICE))
print("my name is moster",name)
""" operator """
# arithmaric operator(+,-,*,/,%)/ and all sign is use for work with operands.
a=3
b=5
c=a+b
print(c)
d=a-b
print(d)
e=a%b
print(e)
f=a*b
print(f)
""" Relational operator"""
a=10
b= 20
print(a==b)# false output  
print(a!=b)# true output# 
print(a<b)#true output
print(a>b)# false output
print(a>=b)# false outpout  
print(a<=b)# true output
# logical operator
a= True
b= False
print(a and b) # false output
print(a or  b ) # true output
print(not a)     # false output
# conversion of data type
m = 1
j = 2.5
print(m+j) # int + float =  float # coversion by automatically
l = (10)
print(j+l) # int + int = int  conversion
# input fiction 
rollno=input("enter your roll no:")
print("Roll no", rollno)
# if we want to covert input value in integer then we use int() funtion with like int (input ())
email_idno =int(input(" enter your eamil id no : "))
print(type(email_idno))
# if we want to floaat input value  in flaot then we use float() funtion with like flaot(input())
mn=float(input("enter ur phone no : "))
print(type(mn))          
uxi=int(input("h:")) 
uvi=int(input("f:"))
"""stringfunction""" # every funtion is work with () bracket is necessary to use with function.
print("sum:",uxi+uvi)
str= "i am student"
"""endswith function""" # endswith function is use for check string is end with given letter or not.
print(str.endswith("ent"))# output is true because string is end with ent
"""startswith function""" # startswith function is use for check string is starting with given letter or not.
print(str.endswith("i"))# output is false because string is not end with i
print(str.startswith("i"))# output is starting with i so output is true 
"""startswith function""" # startswith function is use for check string is starting with given letter or not.
print(str.startswith("am"))# output is false because string is not starting with am 
"""capitalize function""" # capitalize function is use for first letter is capital letter and all letter is small letter.
print("i".capitalize())# output is I am student because first letter is capital letter so output is I am student
# str.replace() function is used for replace any  string wards & character with another string wards & character.
print(str.replace("m","i"))# output is i im student because m is replace with i
print(str.replace("student","BANTI"))# output is i am student because stuent is replace with student
# str.findword () funtion is used to find the word and any chracter in our string 
print(str.find("m")) # find the o in our  string and give the  proper index postion 
print(str.count("i")) # count the i in our string and give the total number of i in our string
# conditonal statement in which we used if, elife, else statent from python programme 
myage = 23
if(myage>=18):
    print("i do haccking") # if condition is true then this statement is print
if(myage<=19):
    print("i fuck anybody")# if condition is false then this statement is not print
    
