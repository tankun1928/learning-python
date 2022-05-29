''' --------------------------
Put your functions here 
------------------------------'''

def read():
    while True:
        x = int(input("Please enter a positive integer: "))
        if x > 0:
            return x
        print("Invalid input value. Please try again.")
        

def findPower(base, power):
    return base ** power