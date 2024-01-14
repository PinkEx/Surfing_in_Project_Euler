from collections import defaultdict
from sympy import factorint
from math import comb

n = 51
fc = []

def prework():
    for i in range(n):
        fc.append(factorint(i))

def C(m: int, k: int):
    v = defaultdict(int)
    for i in range(m, m - k, -1):
        for e in fc[i].keys():
            v[e] += fc[i][e]
    for i in range(k, 0, -1):
        for e in fc[i].keys():
            v[e] -= fc[i][e]
    print(m, k, v)
    return v

def search():
    sqf = []
    for m in range(1, n):
        for k in range(m):
            fc_cmk = C(m, k)
            flag = True
            for p in fc_cmk.keys():
                if fc_cmk[p] > 1:
                    flag = False
                    break
            if flag:
                sqf.append(comb(m, k))
    sqf = list(set(sqf))
    print(len(sqf), sum(sqf))
    print(sqf)
prework()
search()

# Congratulations, the answer you gave to problem 203 is correct.

# You are the 9546th person to have solved this problem.

# This problem has a difficulty rating of 25%. The highest difficulty rating you have solved so far is 65%.
