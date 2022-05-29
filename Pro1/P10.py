print("Hi! I am a smart cashier!")
food_cost = input("Enter the food cost: ")
amount = input("Enter the amount you pay: ")
food_cost = int(food_cost)
amount = int(amount)
amount_change = amount - food_cost
bill1 = amount_change / 1000
bill1 = int(bill1)
total_bill1 = (bill1 * 1000) - amount_change
total_bill1 = abs(total_bill1)

bill2 = total_bill1 / 500
bill2 = int(bill2)
total_bill2 = (bill1 * 1000) + (bill2 * 500) - amount_change
total_bill2 = abs(total_bill2)

bill3 = total_bill2 / 100
bill3 = int(bill3)
total_bill3 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) - amount_change
total_bill3 = abs(total_bill3)

bill4 = total_bill3 / 50
bill4 = int(bill4)
total_bill4 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) + (bill4 * 50) - amount_change
total_bill4 = abs(total_bill4)

bill5 = total_bill4 / 20
bill5 = int(bill5)
total_bill5 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) + (bill4 * 50) +(bill5 * 20) - amount_change
total_bill5 = abs(total_bill5)

bill6 = total_bill5 / 10
bill6 = int(bill6)
total_bill6 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) + (bill4 * 50) +(bill5 * 20) + (bill6 * 10) - amount_change
total_bill6 = abs(total_bill6)

bill7 = total_bill6 / 5
bill7 = int(bill7)
total_bill7 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) + (bill4 * 50) +(bill5 * 20) + (bill6 * 10) + (bill7 * 5) - amount_change
total_bill7 = abs(total_bill7)

bill8 = total_bill7 / 1
bill8 = int(bill8)
total_bill8 = (bill1 * 1000) + (bill2 * 500) + (bill3 * 100) + (bill4 * 50) +(bill5 * 20) + (bill6 * 10) + (bill7 * 5) + (bill8 * 1) - amount_change
total_bill8 = abs(total_bill8)
print()
print("Amount of change = ", amount_change)
print("        ", bill1, "       1000-Baht bill(s)")
print("        ", bill2, "       500-Baht bill(s)")
print("        ", bill3, "       100-Baht bill(s)")
print("        ", bill4, "       50-Baht bill(s)")
print("        ", bill5, "       20-Baht bill(s)")
print("        ", bill6, "       10-Baht coin(s)")
print("        ", bill7, "       5-Baht coin(s)")
print("        ", bill8, "       1-Baht coin(s)")