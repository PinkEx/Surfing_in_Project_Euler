from math import comb

MOD = 1000000123
def digital_DP(L, used_odd):
    ret = 0
    T = ((2 ** used_odd) - 1) * 2
    m = 5 + used_odd
    c = [int(t == 0) for t in range(2 ** 10)]
    for n in range(L):
        c_hat = [0] * (2 ** m)
        for t in range(2 ** m):
            for i in range(int(n == 0), m):
                c_hat[t] += c[t ^ (1 << i)]
        c = c_hat
        ret += c[T] % MOD
    
    return ret % MOD

L, ans = int(input()), 0

for ban in range(6):
    ans += digital_DP(L, 5 - ban) * comb(5, ban) % MOD

print(ans % MOD)