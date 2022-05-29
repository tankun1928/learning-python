# repeatedly get input from an user
# stop when the number is not positive
n = 1 
while n > 0: # condition to continue
    n = int(input("Enter a positive num: "))
print("-------Stop-------") 

while True: # forever loop
    n = int(input("Enter a positive num: "))
    if n < 0: # condition to stop or break
        break # get out of the loop
print("-----Stop-----")
