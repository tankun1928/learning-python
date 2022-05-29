v1_list = input('Enter 13 integers: ').split()
symmetric = False

if len(v1_list) != 13:
   print('Expect', 13, 'values. Found', v1_list, '.')
   exit(1)

checklist = []
checkSymmetric = 0

for entry in v1_list:
   checklist.append(int(entry))

for i in range(len(checklist)):
    if checklist[i] == checklist[12-i]:
        checkSymmetric = checkSymmetric + 1

if checkSymmetric >= 12:
    symmetric = True

if symmetric == True :
    print("Symmetric.")
else :
    print("Not symmetric.")
