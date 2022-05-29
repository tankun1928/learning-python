n = int(input("Number of items in a list: "))
mylist = input("Enter %d integers for the list: " % n).split()
mylist = list(map(int, mylist))
x = int(input("Enter x: "))

# mylist put in increasing order
# print(mylist)
# mylist.insert(1, 10) # .insert(pos, value)
# print(mylist)
# mylist.pop() # remove last item
# print(mylist)
# mylist.pop(3) # remove item at index 3
# print(mylist)

# insert x in order
# 1 2 3 4 5 7 8 9 10
# insert 6
# 1) find position where mylist[i] >= x for the first time
# 2) insert at i
# Method #1
isDone = False # flag
for i in range(len(mylist)):
    if mylist[i] >= x:
        print("Insert at", i)
        mylist.insert(i, x)
        isDone = True
        break

if not isDone:
    print("Insert at", len(mylist))
    mylist.append(x)
print(mylist)

print("--- Method #2 ---")
n = int(input("Number of items in a list: "))
mylist = input("Enter %d integers for the list: " % n).split()
mylist = list(map(int, mylist))
x = int(input("Enter x: "))
for i in range(len(mylist)):
    if mylist[i] >= x:
        print("Insert at", i)
        mylist.insert(i, x)
        break
else: #
    print("Insert at", len(mylist))
    mylist.append(x)

print(mylist)