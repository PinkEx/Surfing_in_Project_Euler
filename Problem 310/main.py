from math import comb, sqrt
from tqdm import trange
n = int(input())
sg = [0] * (n + 1)
sg[1] = 1
for i in trange(2, n + 1):
    smex = [-1]
    for j in range(1, int(sqrt(i)) + 1):
        smex.append(sg[i - j * j])
    smex = list(sorted(smex))
    ans = smex[-1] + 1
    for j in range(1, len(smex)):
        if smex[j] - smex[j - 1] > 1:
            ans = smex[j - 1] + 1
            break
    sg[i] = ans

mx = max(sg)
cnt = [0] * (mx + 1)
for i in range(n + 1):
    cnt[sg[i]] += 1

# print(cnt, sg)

# brute force
# ans = 0
# for a in range(n + 1):
#     for b in range(a, n + 1):
#         for c in range(b, n + 1):
#             if sg[a] ^ sg[b] ^ sg[c] == 0: ans += 1
# print(ans)

ans = 0
# sg[x], sg[y], sg[z] are pairwise different -> x, y, z are pairwise different
for a in range(mx + 1):
    for b in range(a + 1, mx + 1):
        for c in range(b + 1, mx + 1):
            if a != b and a != c and b != c and a ^ b ^ c == 0:
                ans += cnt[a] * cnt[b] * cnt[c]
# sg[x], sg[y], sg[z] has a pair of identical number -- SGs should be 0, 0, 0 or 0, a, a(/a, 0, a/a, a, 0)
# sg[x], sg[y], sg[z] = 0, 0, 0
# x, y, z are pairwise different
ans += comb(cnt[0], 3)
# x, y, z has exactly a pair of identical number
ans += comb(cnt[0], 2) * 2
# x = y = z
ans += cnt[0]
# two of sg[x], sg[y], sg[z] to be a(a is non-zero)
for a in range(1, mx + 1):
    # sg[?1] = sg[?2] = a, ?1 ≠ ?2
    ans += comb(cnt[a], 2) * cnt[0]
    # sg[?1] = sg[?2] = a, ?1 = ?2
    ans += cnt[a] * cnt[0]

print(ans)

# Congratulations, the answer you gave to problem 310 is correct.

# You are the 1227th person to have solved this problem.

# This problem has a difficulty rating of 40%. The highest difficulty rating you have solved so far is 65%.