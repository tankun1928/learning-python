height = float(input("Enter height: "))
price = float(input("Enter price: "))
# Method 1
# if height < 90:
#    print("free")
# if height >= 90 and height < 120:
#   print("half")
# if height >= 120:
#    print("Full") 
# Methid 2
if height < 90:
    print("free")
else: #height >= 90 
    if height < 120:
        print("half")
    else: # height >= 120 
        print("Full") 
# Method 3
if height < 90:
    print("free")
    pay =  0
elif height < 120: # height >= 90
    print("half")
    pay = 0.5 * price
else: # height >= 120 
    print("full")
    pay = price
print("You pay %.2f Bath." % pay)    