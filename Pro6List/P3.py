v1 = input("Enter values of the vector: ").split()
v1 = list(map(float, v1))

v2 = input("Enter values of the vector: ").split()
v2 = list(map(float, v2))
print("v1:", v1)
print("v2:", v2)
#v3 = v1 + v2 # list concatenation
# assume len(v1) == len(v2)
v3 = []
for i in range(len(v1)):
    v3.append(v1[i] + v2[i])
print("v1 + v2 =", v3)
