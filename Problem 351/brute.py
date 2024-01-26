from math import gcd
def calc(n: int):
    ret = n - 1
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if gcd(i, j) != 1: ret += 1
    return ret

n = int(input())
ans = calc(n) * 6
print(ans)