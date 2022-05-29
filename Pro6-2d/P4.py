a = [(2,44,66),(50,50,45)]
b = [(33,44,55),(50,50,50)]
cd = []
dc = []
c = []

for i in range(0,3):
    d = []
    if a[0][i] < b[0][i]:
        print("[0][%d]: A < B"% i)
        d.insert(i, -1)
        cd.extend(d)
    elif a[0][i] == b[0][i]:
        print("[0][%d]: A == B"% i)
        d.insert(i, 0)
        cd.extend(d)
    elif a[0][i] > b[0][i]:
        print("[0][%d]: A > B"% i)
        d.insert(i, 1)
        cd.extend(d)

for i in range(0,3):
    d2 = []
    if a[1][i] < b[1][i]:
        print("[1][%d]: A < B"% i)
        d2.insert(i, -1)
        dc.extend(d2)
    elif a[1][i] == b[1][i]:
        print("[1][%d]: A == B"% i)
        d2.insert(i, 0)
        dc.extend(d2)
    elif a[1][i] > b[1][i]:
        print("[1][%d]: A > B"% i)
        d2.insert(i, 1)
        dc.extend(d2)
        
cd = list(map(int, cd))
dc = list(map(int, dc))
c.append(cd)
c.append(dc)

print("List c:")

for item in c:
    for thing in item:
        print(thing, end="\t")
    print()