from math import sqrt

n, num = int(input()), 0

def calc_period(x):
    s = int(sqrt(x))
    b = x - s * s
    a, c = 0, s
    while True:
        if x > (c - b) ** 2:
            a += 1
            c -= b
        else:
            c = -c
            break
    coes = [{"a": a, "b": b, "c": c}]
    while True:
        s = coes[-1]["a"]
        b = (x - coes[-1]["c"] * coes[-1]["c"]) // coes[-1]["b"]
        a, c = 0, coes[-1]["c"]
        while True:
            if x > (c - b) ** 2:
                a += 1
                c -= b
            else:
                c = -c
                break
        is_duplicate = any(entry == {"a": a, "b": b, "c": c} for entry in coes)
        if is_duplicate:
            break
        coes.append({"a": a, "b": b, "c": c})
    # print(coes)
    return len(coes)

def check_square(x):
    s = int(sqrt(x))
    return s * s == x

for i in range(n + 1):
    if not check_square(i):
        prd = calc_period(i)
        # print(i, prd)
        num += calc_period(i) & 1
print(num)

# Congratulations, the answer you gave to problem 64 is correct.

# You are the 23687th person to have solved this problem.

# This problem has a difficulty rating of 20%. The highest difficulty rating you had previously solved was 5%. 
# This is a new record. Well done!