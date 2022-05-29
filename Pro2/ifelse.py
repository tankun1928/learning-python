age = int(input("Enter age: "))
print("Your age is %d" % age)
isYoung = age < 18 #True / False
print(isYoung) 
# condition
# conparison => True / False
# num value: 0 => False, non-zero => True
# boolean variable
if isYoung: 
    # if isYoung => True 
    print("You cannot vote")
else: # if is Young => False
    print("You can vote")
