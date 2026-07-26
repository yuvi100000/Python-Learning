# strings are immutable sequences of characters.
str1 = "yuvraj is lucky guy. \n he is a good boy ."
print(str1)
# 2 string ko jodne ko concatenation kehte hai.
str2 = "yuvraj age "
str3 = "is 19."
str4 = str2 + str3
print(str4)
# length of string jo string ke characters ki sankhya ko batata hai.
print(len(str2))
# string indexing
str5 = "yuvraj"
print(str5[0]) # y
print(str5[1]) # u
print(str5[2]) # v
print(str5[3]) # r      
print(str5[4]) # a
print(str5[5]) # j
""" if we check the string length"""
string5 = "yuvi"
print(len(string5)) # output is 4 because no space
# indexing 
#it is a position of any string charaffter counting from left to right starting with 0.
print(string5[0]) # y
print(string5[1]) # u
print(string5[2]) # v
print(string5[3]) # i
""" if we acces the index chractre"""
string5 = "yuvi"
ch = string5[0]
print(ch) # output is y
# slicing 
string5 = "yuvi"
print(string5[:4]) # output is yuvi because it will print from index 0 to 3