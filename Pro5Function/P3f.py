''' --------------------------
Put your functions here 
------------------------------'''

def getInput():
    while True:
        x = int(input("Enter a 2-digit number: "))
        if x >=0 or x<100:
            return x
        

def Lottery(lot,guess):
    if lot == guess:
        print("Congratulations!")
    elif (lot-10) == guess or (lot+10) == guess:
        print("Almost got it")
    else:
        print("No, sorry :(")