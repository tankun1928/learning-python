''' --------------------------
Do not change anything here 
------------------------------'''
import P3f
import random

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    lot = random.randrange(0,100)
    guess = P3f.getInput()
    y = P3f.Lottery(lot,guess)
    print("lottery number = %d" %lot)