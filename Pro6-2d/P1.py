row,column = input("Enter 2D list size (row,col): ").split()
row = int(row)
column = int(row)
matrix = []

for i in range(row):
    e = input("Enter %d integers for row %d: "%(column,i)).split()
    e = list(map(int, e)) 
    matrix.append(e)

print("In order:")
for item in matrix:
    for thing in item:
        print(thing, end="\t")
    print()

print("Reverse col, same row:")
for line in matrix:
    line.reverse()
    for number in line:
        print(number, end="\t")
    line.reverse()
    print()

print("Same col, reverse row:")
matrix.reverse()
for line in matrix:
    for number in line:
        print(number, end="\t")
    print()
matrix.reverse()

print("Reverse col, reverse row:")
matrix.reverse()
for line in matrix:
    line.reverse()
    for number in line:
        print(number, end="\t")
    line.reverse()
    print()
matrix.reverse()
