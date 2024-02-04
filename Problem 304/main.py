from sympy import nextprime
from tqdm import trange

def matrix_multiply_mod(A, B, mod):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def matrix_power_mod(matrix, n, mod):
    result = [[1, 0], [0, 1]]  # 初始化为单位矩阵
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply_mod(result, matrix, mod)
        matrix = matrix_multiply_mod(matrix, matrix, mod)
        n //= 2
    return result

def fibonacci_mod(n, mod):
    matrix = [[1, 1], [1, 0]]
    return matrix_power_mod(matrix, n, mod)[0][1]

def f(n):
    mod = 1234567891011
    return fibonacci_mod(n, mod)

n = int(1e5)
a = [0, nextprime(int(1e14))]
b = [0, f(a[-1])]
for i in trange(2, n + 1):
    a.append(nextprime(a[-1]))
    b.append(f(a[-1]))

mod = 1234567891011
print(sum(b) % mod)

# Congratulations, the answer you gave to problem 304 is correct.

# You are the 2318th person to have solved this problem.

# This problem has a difficulty rating of 40%. The highest difficulty rating you have solved so far is 65%. 