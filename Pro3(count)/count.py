i = 0 # initialization
# while
n = int(input("Enter n: "))
i = 0
while i < n: # condition # or i = num that you want
    i += 1 # update
    print(i + 1)
    
print("--------")
# For
# range(n) => 0, 1,...., n-1
# range(1,n) => 1, 2,....., n-1
# range(1,n+1) => 1,2,.....,n
# j = 0, task, j += 1, task, j += 1....
for j in range(1,n+1):
    print(j)