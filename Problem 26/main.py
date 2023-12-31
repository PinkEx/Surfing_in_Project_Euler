
def calc(x):
    p = 1
    while True:
        if (10 ** p - 1) % x == 0:
            return p
        p += 1

n, ans, mx = 1000, -1, 0
for i in range(2, n):
    if i % 2 == 0 or i % 5 == 0: continue
    v = calc(i)
    if v > mx:
        mx, ans = v, i
print(ans, mx)

# Congratulations, the answer you gave to problem 26 is correct.

# You are the 88675th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 