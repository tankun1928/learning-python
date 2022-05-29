Order = input("The order for table: ")
Dish = input("Dish item: ")
dish_howmany = input("How many: ") 
Dishitem2 = input("Dish item: ")
dishitem2_howmany = input("How many: ")
Dishitem3 = input("Dish item: ")
dishitem3_howmany = input("How many: ")

Dish = str(Dish)
Dishitem2 = str(Dishitem2)
Dishitem3 = str(Dishitem3)

dish_howmany = int(dish_howmany)
dishitem2_howmany = int(dishitem2_howmany)
Dishitem3_howmany = int(dishitem3_howmany)
total_dishes = dish_howmany + dishitem2_howmany + Dishitem3_howmany

print()
print("=================================")
print("Order for Table %s" % (Order))
print("* %s : %i" % (Dish, dish_howmany))
print("* %s : %i" % (Dishitem2, dishitem2_howmany))
print("* %s : %s" % (Dishitem3, dishitem3_howmany))
print("Total items : %i " % (total_dishes))
