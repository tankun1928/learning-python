def rdIncome():
    x = int(input("Enter your income: "))
    return x

def isValid(income):
    if income >= 0 and income <= 1000000:
        return True
    else:
        return False

def compTax(income):
    if income < 150000:
        tax = 0
        return tax
    elif income < 500000:
        tax = (income-150000)*0.10
        return tax
    else :
        tax = (income-500000)*0.20 + 35000
        return tax