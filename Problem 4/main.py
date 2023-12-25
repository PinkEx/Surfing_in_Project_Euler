n, ans = int(input()), 0

def check(x):
    x_str = str(x)
    l = len(x_str)
    for i in range(l // 2):
        if x_str[i] != x_str[l - 1 - i]:
            return False
    return True

def p10(p):
    return 10 ** p

for x in range(p10(n - 1), p10(n)):
    for y in range(p10(n - 1), p10(n)):
        if check(x * y):
            ans = max(ans, x * y)
print(ans)

# Congratulations, the answer you gave to problem 4 is correct.

# You are the 500644th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

# Not enough data to determine solve metrics.