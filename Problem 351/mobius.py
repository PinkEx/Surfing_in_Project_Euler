from math import gcd
from sympy import mobius

def calc(n: int):
    tot = n * (n - 1) // 2
    sub = 0
    prime = []
    isprime = [1] * (n + 1)
    mu = [1] * (n + 1)
    for d in range(1, n + 1):
        if d > 1:
            if isprime[d]:
                prime.append(d)
                mu[d] = -1
        for p in prime:
            if d * p > n: break
            isprime[d * p] = 0
            if d % p == 0:
                mu[d * p] = 0
                break
            else: mu[d * p] = -mu[d]
        sub += mu[d] * ((n - 1) // d * (n // d) - (n - 1) // d * ((n - 1) // d + 1) // 2)
    return n - 1 + tot - sub

n = int(input())
ans = calc(n) * 6
print(ans)

# Congratulations, the answer you gave to problem 351 is correct.

# You are the 2703rd person to have solved this problem.

# This problem has a difficulty rating of 25%. The highest difficulty rating you have solved so far is 65%. 