fn2 = 0
fn1 = 1
fn = 1
n = int(input("How many days? "))
if n == 0:
    fn = 0
elif n == 1:
    fn = 1  
else:
    i = 2
    while i <= n:
        fn = fn1 + fn2 # main cal
        i += 1
        fn2 = fn1 # update for next round
        fn1 = fn # update for next round
print("%d-day height is %d cm." % (n, fn))