lim = int(input())
a = [1, 3]
b = [0, 1]
while a[-1] + b[-1] < lim:
    a.append(6 * a[-1] - a[-2] - 2)
    b.append(6 * b[-1] - b[-2])
    print(a[-1], b[-1])
print(a[-1])

# Congratulations, the answer you gave to problem 100 is correct.

# You are the 17434th person to have solved this problem.

# This problem has a difficulty rating of 30%. The highest difficulty rating you had previously solved was 20%. 
# This is a new record. Well done!