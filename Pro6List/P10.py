v1_list = input('Enter 10 integers: ').split()

if len(v1_list) != 10:
   print('Expect', 10, 'values. Found', v1_list, '.')
   exit(1)

uniquelist = []

for i in v1_list:
    if i not in uniquelist:
        uniquelist.append(i)

print("Unique numbers:",end = " ")

for item in uniquelist:
    print(item,end = " ")