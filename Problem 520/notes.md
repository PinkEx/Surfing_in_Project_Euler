PS: 题目看错了，以为是求sum，结果是求count……

# 数位DP

二进制压缩状态 $t (0 \leq t < 2 ^ {10})$，表示各数字当前出现次数的奇偶性。

由于奇数数字出现的次数是 $0, 1, 3, 5, \dots$，需要用一个 $2 ^ 5$ 的枚举去枚举没有出现过的奇数数字，并令：

$$
e_i = 
\begin{cases}
1, IsEven(i) \lor (IsOdd(i) \land \lnot NotAppear(i)) \\
0, IsOdd(i) \land NotAppear(i)
\end{cases}
$$

$e_i$ 起到了掩码的作用。

考虑从高位到低位枚举进行数位DP。（首位非零）

设 $c(t)$ 为到达**当前位**时数字状态为 $t$ 的方案数，$s(t)$ 为到达**当前位**时数字状态为 $t$ 的所有方案之和。

则

$$
\hat c_t = \sum_{i = 0} ^ 9 c_{t \oplus 2 ^ i} e_i
$$

$$
\hat s_t = \sum_{i = 0} ^ 9 (s_{t \oplus 2 ^ i} * 10 + c_{t \oplus 2 ^ i} * i) *  e_i
$$

设位数为 $L$，这样最后 $c(T)$ （ $T$ 就是满足条件的那个最终状态）就是满足条件的 $L$ 位数字的个数。

朴素做法可以求 $c(T)$ 和 $s(T)$ 。

