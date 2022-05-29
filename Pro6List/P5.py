n = int(input('Enter a size: '))

v1_list = input('Enter %d integers: '%n).split()

if len(v1_list) != n:
   print('Expect', n, 'values. Found', v1_list, '.')
   exit(1)

v1 = []
for entry in v1_list:
   v1.append(int(entry))

print("In order:")
for i in range(len(v1)):
    print(v1[i],end = " ")

print()

print("Reverse order:")
for i in reversed(v1):
    print(i,end = " ")