food_price = input("Food price: ")
drink_price = input("Drink price: ")

food_price = float(food_price)
drink_price = float(drink_price)
total_price = food_price + drink_price

discount_food = ((food_price)*5/100)
social_discount = total_price - discount_food 
member = ((total_price)*10/100)
discount_member = total_price - member

print("Total Price = %.2f" % total_price, "Baht")
print("Discount after check-in = %.2f" % social_discount, "Baht")
print("If you are a member, you would pay %.2f" % discount_member, "Baht")

