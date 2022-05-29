from ast import operator
import math
operator
x, s, y = input("Enter x op y (+ - * / ^): ").split()
x = float(x)
s = str(s)
y = float(y)
if s == "^":
    r = x ** y
    print("%.2f" % r)
elif s == "+":
    r = x + y
    print("%.2f" % r)
elif s == "-":
    r = x - y
    print("%.2f" % r)
elif s == "*":
    r = x * y
    print("%.2f" % r)
elif s == "/":
    r = x / y
    print("%.2f" % r)
else:
    print("Invalid op")







