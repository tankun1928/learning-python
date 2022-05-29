psum = 0 # sum for positive num
pcount = 0 # count for positive
nsum = 0 # sum for neg num
ncount = 0 # count for neg
while True:
    n = float(input("Enter a number (0 to quit): "))
    if n == 0:
        break
    # n > 0 or n < 0
    if n > 0: # positive
        psum += n
        pcount += 1
    else: # negative
        nsum += n
        ncount += 1

# loop ended
if pcount == 0:
    pavg = 0
else:
    pavg = psum / pcount
print("Pos: sum = %.2f Avg = %.2f" % (psum, pavg))
if ncount == 0:
    navg = 0
else:
    navg = nsum / ncount
print("Neg: sum = %.2f Avg = %.2f" % (nsum, navg))