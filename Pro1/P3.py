print("Welcome to the BMI Helper for Seniors!")
print()
height = float(input("Please enter height (cm): "))
weight = float(input("Please enter weight (kg): "))

#bmi = weight / ((height/100) * (height/100))
h = height / 100
bmi = weight / (h * h)

print("Your BMI is %.6f" % bmi)
print("Your BMI is %.2f" % bmi)