def func(x):
    dl = list(str(x))
    return sum(int(d) ** 2 for d in dl)

n, cnt = 10000000, 0
f = [0 for i in range(n + 1)]

def getf(x):
    if f[x] == x: return x
    f[x] = getf(f[x])
    return f[x]

for i in range(1, n + 1):
    if f[i] == 0:
        f[i] = func(i)

ss = [1, 89, 145, 42, 20, 4, 16, 37, 58]
for s in ss:
    f[s] = s

for i in range(1, n + 1):
    fa = getf(i)
    if fa != 1: cnt += 1

print(cnt)

# Congratulations, the answer you gave to problem 92 is correct.

# You are the 43748th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 