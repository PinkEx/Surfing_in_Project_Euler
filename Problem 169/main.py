from collections import defaultdict
n, ans = int(input()), 1
# if n & 1 == 0: n = n * 2 + 1
n_bin = bin(n)[2:]
L = len(n_bin)

f = defaultdict(int)
def dfs(c_bit, last_need) -> int:
    if str((c_bit, last_need)) in f.keys():
        return f[str((c_bit, last_need))]
    ret = 0
    if c_bit == L:
        return last_need == 0
    if n_bin[c_bit] == '0':
        if last_need:
            ret += dfs(c_bit + 1, 0) + dfs(c_bit + 1, 1)
        else:
            ret += dfs(c_bit + 1, 0)
    else:
        if last_need:
            ret += dfs(c_bit + 1, 1)
        else:
            ret += dfs(c_bit + 1, 1) + dfs(c_bit + 1, 0)
    f[str((c_bit, last_need))] = ret
    return ret

print(dfs(0, 0))

# Congratulations, the answer you gave to problem 169 is correct.

# You are the 5374th person to have solved this problem.

# This problem has a difficulty rating of 50%. The highest difficulty rating you had previously solved was 35%. 
# This is a new record. Well done!

# Return to Problems page.