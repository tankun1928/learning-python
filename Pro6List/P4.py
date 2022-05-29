n = int(input('Please enter a vector length (n): '))

v1_list = input('Enter values of the vector v1: ').split()
v2_list = input('Enter values of the vector v2: ').split()

if len(v1_list) != n:
   print('Expect', n, 'values. Found', v1_list, '.')
   exit(1)
if len(v2_list) != n:
   print('Expect', n, 'values. Found', v2_list, '.')
   exit(1)

v1 = []
v2 = []
for entry in v1_list:
   v1.append(float(entry))
for entry in v2_list:
   v2.append(float(entry))

print("v1:", end = " ")
print(v1)
print("v2:", end = " ")
print(v2)

innerproduct = 0

for i in range(len(v1)):
    innerproduct = innerproduct+(v1[i]*v2[i])

print("inner product = %.4f" % innerproduct)