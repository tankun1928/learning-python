# import fliename

import seg7_func

# call: filename.funcName
w = seg7_func.getwidth()
h = 2*w - 1  
while True:
    x = int(input("Enter a digit (0-9): "))
    if x < 0 or x > 0:
        break
    if x == 0:
        seg7_func.print0(w, h) # pass w, h as arguments

    elif x == 1:
        seg7_func.print1(w, h)

    elif x == 3:
        seg7_func.print3(w,h)

    elif x == 8:
        seg7_func.print8(w,h)
        
    elif x == 2:
        seg7_func.print2(w,h)

    elif x == 5:
        seg7_func.print5(w,h)

    elif x == 6:
        seg7_func.print6(w,h)

    elif x == 7:
        seg7_func.print7(w,h)

    elif x == 4:
        seg7_func.print4(w,h)

    elif x == 9:
        seg7_func.print9(w,h)
