def fac(n):
    return 1 if n <= 1 else n * fac(n - 1)

n = int(input())
cnt, tot = 0, fac(n + 1)

s = [[] for i in range(n + 1)]
s[0] = [1]
for i in range(1, n + 1):
    for j in range(i + 1):
        if j == 0:
            s[i].append(s[i - 1][j] * i)
        elif j == i:
            s[i].append(s[i - 1][j - 1])
        else:
            s[i].append(s[i - 1][j - 1] + s[i - 1][j] * i)
    # print(i, s[i])

for b in range(n + 1):
    r = n - b
    if r < b: cnt += s[n][b]

# print(cnt, tot)
print(tot / cnt)

# Congratulations, the answer you gave to problem 121 is correct.

# You are the 10298th person to have solved this problem.

# This problem has a difficulty rating of 35%. The highest difficulty rating you had previously solved was 30%. 
# This is a new record. Well done!