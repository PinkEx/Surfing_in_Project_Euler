from sympy import isprime

n = int(input())
lb, ub = 10 ** (n - 1), 10 ** n

def digit_set(x):
    s = set(list(str(x)))
    return s

for m in range(lb, ub):
    if not isprime(m): continue
    for d in range(1, min(m - lb, ub - 1 - m)):
        if digit_set(m - d) != digit_set(m): continue
        if digit_set(m + d) != digit_set(m): continue
        if not isprime(m - d): continue
        if not isprime(m + d): continue
        # print(m - d, m, m + d)
        # print(digit_set(m))
        print(m - d, m, m + d, sep='')

# Congratulations, the answer you gave to problem 49 is correct.

# You are the 61223rd person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 