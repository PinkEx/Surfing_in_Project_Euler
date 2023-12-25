def calc_n_digits(x):
    return len(str(x))

n = int(input())
fib = [0, 1]

while calc_n_digits(fib[-1]) < n:
    fib.append(fib[-1] + fib[-2])

print(len(fib) - 1)

# Congratulations, the answer you gave to problem 25 is correct.

# You are the 162130th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 