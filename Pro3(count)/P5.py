debt = float(input("Enter credit card debt: "))
monthly = float(input("Enter monthly payment: "))

month = 0
total = debt

while debt > 0:
    month = month+1
    total = total+(debt*0.015)
    debt = (debt+(debt*0.015))-monthly
    if debt > 0:
        print("Month %d : %.2f" % (month, debt))
    else:
     print("Month %d : Debt is paid off" % month)

print("Total payment = %.2f" % total)
         




