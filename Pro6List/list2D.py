x = [1, 2, 3, 4, 5] 
for item in x:
    print(item)
mylist = [[1,2], [3,4], [5,6], [7,8]]
print("---item--")
for item in mylist: # item is a list
    #print(item)
    for thing in item: # thing is an int
        print(thing, end=" ")
    print()


print("---index--")
for r in range(4):
    for c in range(2):
        print(mylist[r][c], end = " ")
    print()