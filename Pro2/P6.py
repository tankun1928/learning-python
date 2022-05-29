code, price = input("Enter product and price: ").split()
price = float(price)
#print(code{0})
p = 0
t = 0
if code[0] == "S": 
    p = price
    t = 0
elif code[0] == "T": 
    p = price * 100 / 107
    t = price - p
print("Price without tax = %.2f Baht" % p)
print("7%% Tax = %.2f Baht" % t)

