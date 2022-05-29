x = input("Enter x: ")
x = float(x)
i = 0
sum = 0
f = 0
while i <= x:
    f += 1 
    i += (1/f)
    sum += 1
    print("Round %d : sum = %.5f" % (sum, i))
    #x += 1 

