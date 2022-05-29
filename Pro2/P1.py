weight = float(input("Enter package weight: "))
if weight > 0:
    if weight <= 5:
     cost = weight * 20
    elif weight <= 10:
     cost = (5*20) + ((weight-5)*30)   
    else:
     cost = (5*20) + (5*30) + ((weight-10)*40)
    print("Total delivery cost is %.2f Baht" % cost)
else:
    print("Invalid weight. Bye.")
