mylist = []
while True:
    mystr = input("What kind of blessing do you want? ")
    if mystr == "":
        break
    mylist.append(mystr)

print("You are blessed with")
print(mylist)