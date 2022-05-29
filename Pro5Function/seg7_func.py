# function definition
# func name: getWidth
def getWidth():
    while True:
        wid = int(input("Enter width: "))
        if wid < 3:
            print("Invalid width. Please put w >= 3.")
        else:
            return wid

def getDigit():
    while True:
        x = int(input("Enter a digit: "))
        if x > 9 or x < 0:
            print("Invalid digit. Please put 0-9.")
        else:
            return x # return value + exit function

# function arguments : w, h
def print0(w, h):
    print("--- 0 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == h:
                print("*", end=" ")
            elif c == 1 or c == w:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print1(w, h):
    print("--- 1 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if c == w:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print2(w,h):
    print("--- 2 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h:
                print("*", end=" ")
            elif c == w and r <= w: # upper right
                print("*", end=" ")
            elif c == 1 and r >= w: # lower left
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print3(w,h):
    print("--- 3 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h:
                print("*", end=" ")
            elif c == w:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print4(w,h):
    print("--- 4 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == w: # middle row
                print("*", end=" ")
            elif c == w: # right
                print("*", end=" ")
            elif c == 1 and r <= w: # upper left
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print5(w,h):
    print("--- 5 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h:
                print("*", end=" ")
            elif c == 1 and r <= w: # upper left
                print("*", end=" ")
            elif c == w and r >= w: # lower right
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print6(w,h):
    print("--- 6 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h:
                print("*", end=" ")
            elif c == 1: # left
                print("*", end=" ")
            elif c == w and r >= w: # lower right
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print7(w,h):
    print("--- 7 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1:
                print("*", end=" ")
            elif c == w: 
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print8(w,h):
    print("--- 8 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h:
                print("*", end=" ")
            elif c == 1 or c == w:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print9(w,h):
    print("--- 9 ---")
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r == h: 
                print("*", end=" ")
            elif c == w: # right
                print("*", end=" ")
            elif c == 1 and r <= w: # upper left
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# -----------------------------
# Everything starts working from here :: Main part of the program
# -----------------------------
# do the main part if the file is run (as main program)
if __name__ == "__main__":
    # task 1) get size from user
    print("Start at Main")
    w = getWidth()
    print("wid = ", w)
    h = 2*w - 1 # height

    # task 2) get option from user
    x = getDigit()

    # print("--- canvas ---")
    # for r in range(1,h+1):
    #     for c in range(1,w+1):
    #         print("*", end=" ")
    #     print()
    if x == 0:
        print0(w, h) # pass w, h as arguments

    elif x == 1:
        print1(w, h)

    elif x == 3:
        print3(w,h)

    elif x == 8:
        print8(w,h)
        
    elif x == 2:
        print2(w,h)

    elif x == 5:
        print5(w,h)

    elif x == 6:
        print6(w,h)

    elif x == 7:
        print7(w,h)

    elif x == 4:
        print4(w,h)

    elif x == 9:
        print9(w,h)