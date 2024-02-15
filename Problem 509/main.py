from math import comb, sqrt
from tqdm import trange
n = int(input())
l = len(bin(n)) - 2

cnt = [0] * l

cnt[0] = (n + 1) // 2
n = n - cnt[0]
for i in range(1, l):
    cnt[i] = (n + 1) // 2
    n = n - cnt[i]

ans = 0
for sa in range(l):
    for sb in range(l):
        for sc in range(l):
            if sa ^ sb ^ sc != 0: ans += cnt[sa] * cnt[sb] * cnt[sc]
print(ans % 1234567890)

# Congratulations, the answer you gave to problem 509 is correct.

# You are the 613th person to have solved this problem.

# You have earned 1 new award:

# Daring Dozen: Solve twelve problems with an ID containing three digits


# This problem has a difficulty rating of 45%. The highest difficulty rating you have solved so far is 65%.