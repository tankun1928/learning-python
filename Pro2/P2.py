height = float(input("Your height (cm): "))
if height >= 120: # can ride
    print("Yes! You can play.")
else:
    print("Sorry, you need %.2f more cm to play." % (120-height))