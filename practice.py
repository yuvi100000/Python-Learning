name = "BANTI SOLANKI"
print(name)
print(type(name))
print("my name is:", name)
myvariable_1=1
print("myvariable_1:",2)
print(type(myvariable_1))
most = 5.9
print(most)
print(type(most))
a=3
b=5
u=a%b
print(u)
print(type(u))
# arithmatic operators 
bas= 2
nn= 3
lol = (bas == nn),#false because 2 is  equal(==) 3 is not true
print(lol)
bn= 3 
mn =6
print(bn!=mn ) # true  bcz 3 is not (!=) to 6 
k = 4 
p = 1
print(k>p)
print(k<p)
print(k>=p)
print(k<=p)
print(not k>p)
print(k and p )
print (k or p)
# conversion 
tt = 1
oo = 2.0
print(tt+oo) # int + flaot in conversion in float 
yy = 6
ll = 4.0 # float 
print(yy+int(ll)) # int + int(float)
# input the value its wrk aftr the ouput and ask the input value 
input("enter the roll no:")  
monster = input("i want a ak47:",)
print("i am monster i want AK 47:",monster)
phn = int(input("enter ur phone no :" ))
print(type(phn))
wq="Jashn-e-Ishqa ek aisa geet hai jo pyaar ki khushi, junoon aur uske jashn ko darshata hai. Isme dikhaya gaya hai ki sachcha pyaar zindagi ko khubsurat bana deta hai aur har pal ko ek tyohar jaisa mehsoos karwata hai. Gaana do dilon ke gehre jazbaat, unke bharose aur ek-doosre ke saath bitaaye har lamhe ki khushi ko vyakt karta hai. Iska sangeet aur bhavnaayein pyaar ki taqat, ummeed aur saath milkar zindagi jeene ki khoobsurti ko ubhaarti hain."
print(wq)
str1 = "Jashn-e-Ishqa ek aisa geet hai jo pyaar ki khushi, junoon aur uske jashn ko darshata hai. Isme dikhaya gaya hai ki sachcha pyaar zindagi ko khubsurat bana deta hai aur har pal ko ek tyohar jaisa mehsoos karwata hai. Gaana do dilon ke gehre jazbaat, unke bharose aur ek-doosre ke saath bitaaye har lamhe ki khushi ko vyakt karta hai. Iska sangeet aur bhavnaayein pyaar ki taqat, ummeed aur saath milkar zindagi jeene ki khoobsurti ko ubhaarti hain."
length = len(str1)
print(str1)
 # length of string 
print("length of string=", length)
str = "Banti"
# indexing of string and find the character postion like whih position (0,1,2,3)
ch=str[0]
print(ch), print(str[0])
# slicing in this we found  any string and any value of mid to given position wht we found
print(str[0:4])
# string funtion  in this funtion end of string and wrds if its it  give true value output and not end wrd its false vale in output 
#str.ends with 
str = "i am hack"
print(str.endswith("ack"))
#str.startwith
text = "hacker"
print(text.startswith("h"))
veggis = "onion", "tomato"
for val in veggis:
    print(val)