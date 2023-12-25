n = int(input())

b = []

b.append([1])

for m in range(n):
    b.append(b[-1])
    l = len(b[-1])
    for i in range(l):
        b[-1][i] *= 2
    i = 0
    while i < len(b[-1]):
        if b[-1][i] >= 10:
            if i + 1 == l:
                b[-1].append(0)
            b[-1][i + 1] += b[-1][i] // 10
            b[-1][i] %= 10
        i += 1
# print(b[-1])
print(sum(b[-1]))

# Congratulations, the answer you gave to problem 16 is correct.

# You are the 237937th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

# Not enough data to determine solve metrics.