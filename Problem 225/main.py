from sympy import factorint, isprime
import time

no = 124
pmax = 6669
P = set()

for x in range(3, pmax):
    if isprime(x): P.add(x)

P = sorted(list(P))
E = [0 for i in range(len(P))]

def check_tribo_mod_n(n):
    ptr = set()
    f = [1, 1, 1]
    while True:
        if f[-1] == 0:
            return False
        if (f[-1], f[-2], f[-3]) in ptr: break
        ptr.add((f[-1], f[-2], f[-3]))
        f.append((f[-1] + f[-2] + f[-3]) % n)
    print(n)
    return True

nd = []
for n in range(27, pmax + 1):
    if n & 1 and check_tribo_mod_n(n):
        nd.append(n)
        if len(nd) == no: break
print(nd[-1])

# Congratulations, the answer you gave to problem 225 is correct.

# You are the 4664th person to have solved this problem.

# This problem has a difficulty rating of 45%. The highest difficulty rating you have solved so far is 65%.