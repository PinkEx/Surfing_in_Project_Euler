# filename = "example_matrix.txt"
filename = "matrix.txt"
with open(filename) as f:
    lns = f.readlines()
n = len(lns)
a = []
for ln in lns:
    ln = ln.strip()
    a.append(list(map(int, ln.split(','))))

for i in range(n):
    for j in range(n):
        if i | j == 0: continue
        if i > 0 and j > 0:
            a[i][j] += min(a[i - 1][j], a[i][j - 1])
        elif i == 0:
            a[i][j] += a[i][j - 1]
        elif j == 0:
            a[i][j] += a[i - 1][j]
print(a[n - 1][n - 1])

# Congratulations, the answer you gave to problem 81 is correct.

# You are the 36259th person to have solved this problem.

# This problem has a difficulty rating of 10%. The highest difficulty rating you have solved so far is 20%. 