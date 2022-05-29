import math 
math.sqrt
import math
abs

x1, y1, x2, y2 = input("Enter x1, y1, x2, y2: "). split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
Euclidean = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
Manhattan = ((abs(x1 - x2)) + (abs(y1 - y2)))

print("Euclidean distance = %.6f" % Euclidean)
print("Manhattan distance = %.6f" % Manhattan) 



