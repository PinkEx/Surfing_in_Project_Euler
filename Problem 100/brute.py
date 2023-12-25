from math import sqrt

k = 1 + sqrt(2)
n = 10
lim = int(10 ** 13)
find = False
while n <= lim:
    ym = int(n / (1 + k))
    for d in range(-3, 3):
        y = ym + d
        x = n - y
        if (x - y) * (x + y - 1) == 2 * x * y:
            find = True
            print("find!", x, y, ym)
    if n % 1000000 == 0:
        print(n, "searched")
    n += 1
    
