maxv, sum = 4000000, 0
f = [1, 1]
while f[-1] <= maxv:
    f.append(f[-1] + f[-2])
    if f[-1] % 2 == 0: sum += f[-1]
print(sum)

# Congratulations, the answer you gave to problem 2 is correct.

# You are the 785657th person to have solved this problem.

# This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 65%.