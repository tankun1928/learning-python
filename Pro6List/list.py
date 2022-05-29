import random


x = 5
y = 10 
z = 20
# list : room / room number : data slot / index
mylist = [5, 10, 20]
print(type(mylist))
print(mylist)
# listname[index] : index = 0 .... n-1 : n = list size
# len(listname) : lenght of the list
print("list lenght : ", len(mylist)) # find lenght of the list
print(mylist[0]) 
print(mylist[1]) 
print(mylist[2]) 
print("-----")
for i in range(len(mylist)):
    print(i, mylist[i])
# random 100 integrts
# put them into a list 
# print them
intlist = [] # empty list 
for i in range(100):
    r = random.randint(0, 99)
    intlist.append(r)

print(intlist)
for i in range(100):
    print(intlist[i])

print("-----")
for item in intlist:
    print(item)

