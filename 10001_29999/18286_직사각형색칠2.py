from sys import stdin

input = stdin.readline
div = 10 ** 9 + 7


def matrix_multiple(first, second=False):
    if not second:
        second = first
    res = [[0] * s for _ in range(s)]
    for x in range(s):
        for y in range(s):
            for z in range(s):
                res[x][y] += first[x][z] * second[z][y]
            res[x][y] %= div
    return res


n, m = map(int, input().split())
s = 1 << m
mat = [[0] * s for _ in range(s)]
for i in range(s):
    c1 = [1 if (1 << bit) & i else 0 for bit in range(m)]
    for j in range(i, s):
        c2 = [1 if (1 << bit) & j else 0 for bit in range(m)]
        mat[i][j] = 1
        mat[j][i] = 1
        for k in range(m - 1):
            if c1[k] == c1[k + 1] == c2[k] == c2[k + 1]:
                mat[i][j] = 0
                mat[j][i] = 0
                break
e = [[0] * s for _ in range(s)]
for i in range(s):
    e[i][i] = 1
n -= 1
while n > 0:
    if n & 1:
        e = matrix_multiple(mat, e)
    mat = matrix_multiple(mat)
    n //= 2
ans = 0
for i in range(s):
    ans += sum(e[i])
    ans %= div
print(ans)
