
print("=== Membership Application ===")
print()
first_name = input("Please enter the applicant's first name: ") 
last_name = input("Last name: ")
year, month, date = input("Your birthday (year month date): "). split()

year = int(year)
age = 2022 - year

blessing = input("Your blessing: ")
print()
print("Welcome %s, %s (%i / %s / %s , age %i) " % (last_name, first_name, year, month, date, age,))
print(blessing)