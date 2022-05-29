itemlist = []

while True:
   val = input('Item to buy: ')
   n = len(val)
   if n > 0:
       itemlist.append(val)
   else:
       break

itemlists = 0
for i in range(len(itemlist)):
    itemlists = i+1

print('There are %d items in your shopping list:'%itemlists)
print(itemlist)
if itemlists > 5:
    print("Too many items, removing %d last items"%(itemlists-5))
    for i in range(5,itemlists):
        itemlist.pop(5)
    print(itemlist)