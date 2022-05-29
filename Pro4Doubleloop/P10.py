inputloop = True
while inputloop:
    income = input("Net Income: ") 
    if income  == "q" or income == "Q":
        inputloop = False
        print("Bye")
    else:
        income = float(income)
        if income < 0:
            print("Wrong input: negative income.")
        elif income <= 150000:
            tax = 0
            print("Tax = %.2f Baht" % tax)
        elif income <= 300000:
            tax = (income-150000)*0.05
            print("Tax = %.2f Baht" % tax)
        elif income <= 500000:
            tax = (income-300000)*0.10 + 7500 
            print("Tax = %.2f Baht" % tax)
        elif income <= 750000:
            tax = (income-500000)*0.15 + 7500 + 20000 
            print("Tax = %.2f Baht" % tax)
        elif income <= 1000000:
            tax = (income-750000)*0.20 + 7500 + 20000 + 37500 
            print("Tax = %.2f Baht" % tax)
        elif income <= 2000000:
            tax = (income-1000000)*0.25 + 7500 + 20000 + 37500 + 50000 
            print("Tax = %.2f Baht" % tax)
        elif income <= 5000000:
            tax = (income-2000000)*0.30 + 7500 + 20000 + 37500 + 50000 + 250000 
            print("Tax = %.2f Baht" % tax)
        else:
            tax = (income-5000000)*0.35 + 7500 + 20000 + 37500 + 50000 + 250000 + 900000 
            print("Tax = %.2f Baht" % tax)