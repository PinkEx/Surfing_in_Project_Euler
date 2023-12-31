f = {1: 1}
def func(x):
    if x in f.keys():
        return f[x]
    else:
        v = func(3 * x + 1 if x % 2 == 1 else x // 2)
        f[x] = v + 1
        return v + 1

n, mx, ans = 1000000, 1, 1
for i in range(2, n + 1):
    v = func(i)
    if v > mx:
        mx = v
        ans = i
    mx = max(mx, func(i))

print(ans, mx)

# Congratulations, the answer you gave to problem 14 is correct.

# You are the 235864th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 