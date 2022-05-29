''' --------------------------
Do not change anything here 
------------------------------'''
import P8f

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    # n,k = input("Enter n and k: ").split()
    # n = int(n)
    # k = int(k)
    myin = input("Enter n and k: ").split()
    #print(myin)
    n, k = list(map(int, myin))
    #print(n, type(n), k, type(k))
    c = P8f.fact(n) / (P8f.fact(k) * P8f.fact(n-k))
    print("C(%d,%d) = %d" %(n,k,c))