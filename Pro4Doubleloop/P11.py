w = int(input("Enter size: "))
h = 2*w - 1
while True:
    x = int(input("Enter a digit (0-9): "))
    if x == 1:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if c == w:
                    print("*",end=" ")   
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x ==2:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == w and r <= w:
                    print("*",end=" ")
                elif c == 1 and r >= w:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x ==3:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 4:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == w:
                    print("*",end=" ")  
                elif c == w:
                    print("*",end=" ")
                elif c == 1 and r <= w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 5:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == w and w <= r:
                    print("*",end=" ")
                elif c == 1 and w >= r:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 6:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == w and w <= r:
                    print("*",end=" ")
                elif c == 1 and w >= r:
                    print("*",end=" ")
                elif c == 1 and r >= w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 7:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 :
                    print("*",end=" ")  
                elif c == w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 8:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == 1 or c == w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 9:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c == w and w <= r:
                    print("*",end=" ")
                elif c == 1 and w >= r:
                    print("*",end=" ")
                elif c == w and r <= w:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
            print()
        pass
    elif x == 0:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == h:
                    print("*",end=" ")  
                elif c == 1 or c == w:
                    print("*",end=" ")  
                else:
                    print(" ",end=" ")
            print()
        pass
    else:
        print("Bye!")
        break
    
