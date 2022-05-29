a = 9
# selection
if a > 0:
    print("xx")
else:
    print("Nope")
# iteration / loop
while a > 0:
    print(a, ": xx")
    a -= 1
print("------")
print(range(9))
for i in range(9):
    print(i, ": xx")
print("------")
# print x5 times for each line
# do this for 10 times
for d in range(1,11): # loop outside
    # for each day
    for r in range(1,6): # loop inside
        print(d,r,"x")
    print()

for d in range(1,11): # loop outside
    # for each day
    for r in range(1,6): # loop inside
        print("x", end=" ") # บรรทัดเดียวกัน
    print()

for d in range(1,11): # loop outside
    # for each day
    for r in range(1,6): # loop inside
        print("x", end=" ") # บรรทัดเดียวกัน
    print()


