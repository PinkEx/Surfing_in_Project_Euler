def check_palindromic(x):
    x_str = str(x)
    l = len(x_str)
    for i in range(l // 2):
        if x_str[i] != x_str[l - 1 - i]:
            return False
    x_str = str(bin(x))[2:]
    l = len(x_str)
    for i in range(l // 2):
        if x_str[i] != x_str[l - 1 - i]:
            return False
    return True

n, sum = int(input()), 0
for i in range(n):
    if check_palindromic(i):
        sum += i
print(sum)

# Congratulations, the answer you gave to problem 36 is correct.

# You are the 93176th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.