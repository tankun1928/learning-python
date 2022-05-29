n = 9
print("--- filled box ---")
for r in range(1, n+1):
    for c in range(1, n+1):
        print("*", end=" ")
    print()

print("--- empty box ---")
for r in range(1, n+1):
    for c in range(1, n+1):
        if r == 1 or r ==n:
         print("*", end=" ")
        elif c == 1 or c ==n:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()


print("--- plus ---")
for r in range(1, n+1):
    for c in range(1, n+1):
        if r == (n+1)/2: # assume n odd
         print("*", end=" ")
        elif c == (n+1)/2:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()


print("--- ster ---")
for r in range(1, n+1):
    for c in range(1, n+1):
        if r == (n+1)/2: # assume n odd
         print("*", end=" ")
        elif c == (n+1)/2:
            print("*", end=" ")
        elif r == c:
            print("*", end=" ")
        elif r + c == n + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()