MOD = 1000000123
def digital_DP(L, e):
    T = 0
    for i in range(10):
        if e[i] and (i & 1): T |= 1 << i

    c = [0 for t in range(2 ** 10)]
    c[0] = 1
    s = [0 for t in range(2 ** 10)]
    for n in range(L):
        c_hat = [0 for t in range(2 ** 10)]
        s_hat = [0 for t in range(2 ** 10)]
        for t in range(2 ** 10):
            for i in range(int(n == 0), 10):
                c_hat[t] += c[t ^ (1 << i)] * e[i]
                s_hat[t] += (s[t ^ (1 << i)] * 10 + c[t ^ (1 << i)] * i) * e[i]
        c = c_hat.copy()
        s = s_hat.copy()
    
    return c[T] % MOD
    

e = [1 for i in range(10)]
L, ans = int(input()), 0

for na_1 in range(2):
    for na_3 in range(2):
        for na_5 in range(2):
            for na_7 in range(2):
                for na_9 in range(2):
                    e[1], e[3], e[5], e[7], e[9] = 1 - na_1, 1 - na_3, 1 - na_5, 1 - na_7, 1 - na_9
                    ans += digital_DP(L, e)


print(ans % MOD)