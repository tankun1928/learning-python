import P11f

if __name__ == "__main__":
    income = P11f.rdIncome()
    if P11f.isValid(income):
        print("Income: %d" % income)
        print("Tax: %d" % P11f.compTax(income))
    else:
        print("Invalid income.")
