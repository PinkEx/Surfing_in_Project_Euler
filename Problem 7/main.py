from sympy import nextprime

n = int(input())
P = [2]
while len(P) < n:
    P.append(nextprime(P[-1]))

print(P[-1])

# Congratulations, the answer you gave to problem 7 is correct.

# You are the 434189th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%. 