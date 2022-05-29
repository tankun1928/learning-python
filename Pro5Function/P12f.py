def readInput():
    myin = input("Enter 3 numbers: ").split()
    x, y, z = list(map(float, myin))
    return x, y, z


def sort(x,y,z):
    sortprit = [x,y,z]
    sortprit.sort()
    return sortprit