# VAriable and data type

# number: integer, floating-point
from turtle import st


x=  3
y= 3.0
print(x, type(x))
print(y, type(y))

# text: string
str1= "Thankhun"
str2= "Nuekchop"
print(str1, type(str1), str2, type(str2))
str3=str1+str2 #string concatenation
print(str3)
str4 = str1 +" "+ str2
print(str4)
a=16 
b=75
print("I am ", a, "years old.")
print("My weight is", b, "kgs.")

print("I am", a, ".")
print("I am %d." % a) # formatted string
# %d : int, : float, %s : string
print("I am %d. My weight is %f kgs." % (a, b))
print("I am %d. My weight is %.2f kgs." % (a, b))
print("I am %d. My weight is %.10f kgs." % (a, b))