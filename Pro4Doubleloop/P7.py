n = int(input("Enter n: "))
for i in range (n):
    for t in range (i, n):
        print(" ", end=" ")

    for t in range (i+1):
        print('*', end=' ')
    print()