from math import comb, sqrt
from tqdm import trange
n = int(input())
sg = [0] * (n + 1)
sg[1] = 0
for i in trange(2, n + 1):
    smex = [-1]
    for j in range(1, i // 2 + 1):
        if i % j != 0: continue
        smex.append(sg[i - j])
    smex = list(sorted(smex))
    ans = smex[-1] + 1
    for j in range(1, len(smex)):
        if smex[j] - smex[j - 1] > 1:
            ans = smex[j - 1] + 1
            break
    sg[i] = ans

ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            if sg[a] ^ sg[b] ^ sg[c] != 0: ans += 1
print(ans)
print(sg)