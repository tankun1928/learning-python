net = input("Net Income: ")
net = float(net)

if net == 0:
    tax = 0
    print("Tax = %.2f Baht" % tax)
elif net < 0:
    print("Wrong input: negative income.")
elif net <= 150000:
    tax = 0
    print("Tax = %.2f Baht" % tax)
elif net == 150001:
    tax = (net - 150000) * 5/100
    print("Tax = %.2f Baht" % tax)
elif net <= 300000:
    tax = (net - 150000) * 5/100
    print("Tax = %.2f Baht" % tax)
elif net == 300001:
    tax = ((net - 300000) * 10/100) + 7500
    print("Tax = %.2f Baht" % tax)
elif net <= 500000:
    tax = ((net - 300000) * 10/100) + 7500
    print("Tax = %.2f Baht" % tax)
elif net == 500001:
    tax = ((net - 500000) * 15/100) + 27500
    print("Tax = %.2f Baht" % tax)
elif net <= 750000:
    tax = ((net - 500000) * 15/100) + 27500
    print("Tax = %.2f Baht" % tax)
elif net == 750001:
    tax = ((net - 750000) * 20/100) + 65000
    print("Tax = %.2f Baht" % tax)
elif net <= 1000000:
    tax = ((net - 750000) * 20/100) + 65000
    print("Tax = %.2f Baht" % tax)
elif net == 1000001:
    tax = ((net - 1000000) * 25/100) + 115000
    print("Tax = %.2f Baht" % tax)
elif net <= 2000000:
    tax = ((net - 1000000) * 25/100) + 115000
    print("Tax = %.2f Baht" % tax)
elif net == 2000001:
    tax = ((net - 2000000) * 30/100) + 365000
    print("Tax = %.2f Baht" % tax)
elif net <= 5000000:
    tax = ((net - 2000000) * 30/100) + 365000
    print("Tax = %.2f Baht" % tax)
elif net >   5000001:
    tax = ((net - 5000000) * 35/100) + 1265000
    print("Tax = %.2f Baht" % tax)
else: 
    print("Wrong input: negative income.")



