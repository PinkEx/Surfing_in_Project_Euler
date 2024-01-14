def r_max(a: int):
    m = a * a
    r_max = 0
    # max{2(2k+1)a mod a^2}
    for k in range(a):
        r_max = max(r_max, 2 * (2 * k + 1) * a % m)
    # this can be reduce to a more general problem: max{a+kb mod m}. This problem has quicker solutions than linear solution.
    return r_max

a_fr, a_to, ans = 3, 1000, 0
for a in range(a_fr, a_to + 1):
    print(a, r_max(a))
    ans += r_max(a)

print(ans)

# Congratulations, the answer you gave to problem 120 is correct.

# You are the 14602nd person to have solved this problem.

# Nice work, p1nk3x, you've just advanced to Level 1.
# 126806 members (12%) have made it this far.

# You have earned 1 new award:

# The Journey Begins: Progress to Level 1 by solving twenty-five problems


# This problem has a difficulty rating of 25%. The highest difficulty rating you have solved so far is 65%. 