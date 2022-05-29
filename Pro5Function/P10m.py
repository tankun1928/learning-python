''' --------------------------
Do not change anything here 
------------------------------'''
from math import sqrt
from P10f import read, findPower

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    A = read()
    B = read()
    C = read()
    D = read()
    #print(A, B, C, D)
    Z = sqrt((findPower(A,B) + findPower(B,C) + findPower(C,D)) / 10.25)
    print("Z = %.5f" % Z)