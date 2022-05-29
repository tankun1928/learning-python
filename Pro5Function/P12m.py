import P12f

if __name__ == "__main__":
    x,y,z = P12f.readInput()
    n1,n2,n3 = P12f.sort(x,y,z)
    print("%.1f <= %.1f <= %.1f"% (n1,n2,n3))