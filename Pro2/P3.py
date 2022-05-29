import math 
math.sqrt
import math
abs

x1, y1, x2, y2  = str(input("Enter x1, y1, x2, y2: ")). split()

print("Please choose your distance:")
print("        1 Euclidean distance")
print("        2 Manhattan distance")
choice = int(input("Your choice: "))
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
Euclidean = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
Manhattan = ((abs(x1 - x2)) + (abs(y1 - y2)))
if choice == 1:
    print("Euclidean distance = %.5f" % Euclidean)
else:
    print("Manhattan distance = %.5f" % Manhattan)
