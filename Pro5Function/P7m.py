''' --------------------------
Do not change anything here 
------------------------------'''
import P7f

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    # fact(n) : return n!
    n = int(input("Enter n: "))
    for i in range(1,n+1):
        f = P7f.fact(i)
        print("%d! = %d" % (i, f))