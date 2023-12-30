with open("Problem 11/input.txt") as f:
    lns = f.readlines()

a = []
for ln in lns:
    a.append(list(map(int, ln.split(' '))))

n, m = len(a), len(a[0])
mm = 0
for i in range(n):
    for j in range(m):
        if i + 3 < n:
            mm = max(mm, a[i][j] * a[i + 1][j] * a[i + 2][j] * a[i + 3][j])
        if j + 3 < m:
            mm = max(mm, a[i][j] * a[i][j + 1] * a[i][j + 2] * a[i][j + 3])
        if i + 3 < n and j + 3 < m:
            mm = max(mm, a[i][j] * a[i + 1][j + 1] * a[i + 2][j + 2] * a[i + 3][j + 3])
        if i + 3 < n and j >= 3:
            mm = max(mm, a[i][j] * a[i + 1][j - 1] * a[i + 2][j - 2] * a[i + 3][j - 3])
print(mm)

# Congratulations, the answer you gave to problem 11 is correct.

# You are the 243628th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 