from math import gcd

n, lcm = int(input()), 1
for i in range(2, n + 1):
    lcm = lcm * i // gcd(lcm, i)
print(lcm)

# Congratulations, the answer you gave to problem 5 is correct.

# You are the 503948th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 
