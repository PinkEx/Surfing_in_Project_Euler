from sympy import isprime

P = set()
nP = set()
def Isprime(x):
    if x in P:
        return True
    if x in nP:
        return False
    ret = isprime(x)
    if ret:
        P.add(x)
    else:
        nP.add(x)
    return ret

def check(n, x):
    fr, to = n * (n - 1) // 2 + 1, n * (n + 1) // 2 + 1
    cnt = Isprime(x + n) + Isprime(x + n + 1)
    if x > fr: cnt += Isprime(x - (n - 1) - 1) + Isprime(x + n - 1)
    if x < to - 1: cnt += Isprime(x - (n - 1))
    if x < to - 2: cnt += Isprime(x - (n - 1) + 1)
    return cnt >= 2

def calc(n):
    ret = 0
    fr, to = n * (n - 1) // 2 + 1, n * (n + 1) // 2 + 1
    for x in range(fr, to):
        if not Isprime(x): continue
        cnt = 0
        if Isprime(x + n):
            cnt += 1
            if check(n + 1, x + n):
                ret += x
                continue
        if Isprime(x + n + 1):
            cnt += 1
            if check(n + 1, x + n + 1):
                ret += x
                continue
        if cnt >= 2:
            ret += x
            continue
        if x > fr:
            if Isprime(x - (n - 1) - 1):
                cnt += 1
                if check(n - 1, x - (n - 1) - 1):
                    ret += x
                    continue
            if cnt >= 2:
                ret += x
                continue
            if Isprime(x + n - 1):
                cnt += 1
                if check(n + 1, x + n - 1):
                    ret += x
                    continue
            if cnt >= 2:
                ret += x
                continue

        if x < to - 1:
            if Isprime(x - (n - 1)):
                cnt += 1
                if check(n - 1, x - (n - 1)):
                    ret += x
                    continue
            if cnt >= 2:
                ret += x
                continue
        if x < to - 2:
            if Isprime(x - (n - 1) + 1):
                cnt += 1
                if check(n - 1, x - (n - 1) + 1):
                    ret += x
                    continue
            if cnt >= 2:
                ret += x
                continue
        if cnt >= 2:
            ret += x
    return ret

n = int(input())
print(calc(n))

# Congratulations, the answer you gave to problem 196 is correct.

# You are the 2728th person to have solved this problem.

# You have earned 1 new award:

# Unlucky Squares: Solve thirteen square numbered problems


# This problem has a difficulty rating of 65%. The highest difficulty rating you had previously solved was 50%. 
# This is a new record. Well done!