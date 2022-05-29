x = input("Enter an integer: ")
y = input("Enter you name: ")
# echo input data
print("Your x is", x, type(x))
print("Your name is", y, type(y))

# convert the input string into an integer
xx = int(input("Enter an integer: "))
print(xx + 3)
zz = float(input("Enter a number: "))
print(zz)

# This is a comment
# Line comment

'''
This is a block comment.
You can type many lines in this block.
And the program will ignore them.

'''
print("Bye...not yet!")

name, last=input("Enter name and lastname: ").split()
print(name)
print(last)

c, d=input("Enter 2 integers: "). split()
print(type(c))
print(type(d))
c = int(c)
d = int(d)
print(type(c))
print(type(d))

myin=input("ENter 4 integers: "). split()
in1, in2, in3, in4=list(map(int, myin))
print(in1)
print(in2)
print(in3)
print(in4)