import math

s = int(input())

for a in range(1, s):
    for b in range(1, min(a, s - a)):
        c = s - a - b
        if a * a + b * b == c * c:
            # print(a, b, c)
            print(a * b * c)

# Congratulations, the answer you gave to problem 9 is correct.

# You are the 369034th person to have solved this problem.

# You have earned 1 new award:

# Baby Steps: Solve three problems


# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

# Not enough data to determine solve metrics.