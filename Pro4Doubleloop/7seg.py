w = 5 # width
h = 2*w - 1 # height
print("--- canvas ---")
for r in range(1,h+1):
    for c in range(1,w+1):
        print("*", end=" ")
    print()
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
print("--- 1 ---")
for r in range(1,h+1):
    for c in range(1,w+1):
        if c == w:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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