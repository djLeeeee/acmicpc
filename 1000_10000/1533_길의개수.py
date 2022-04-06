from sys import stdin

input = stdin.readline


def multiple_matrix(first, second=None):
    if not second:
        second = first
    sz = len(first)
    res = [[0] * sz for _ in range(sz)]
    for jj in range(sz):
        for ii in range(sz):
            for kk in range(sz):
                res[ii][kk] += first[ii][jj] * second[jj][kk]
    for ii in range(sz):
        for jj in range(sz):
            res[ii][jj] %= div
    return res


div = 10 ** 6 + 3
n, s, e, t = map(int, input().split())
table = [[0] * (5 * n) for _ in range(5 * n)]
for i in range(n):
    for k in range(4):
        table[5 * i + k][5 * i + k + 1] = 1
    line = list(map(int, input().strip()))
    for j in range(n):
        x = line[j]
        if x:
            table[5 * i + x - 1][5 * j] = 1
result = [[0] * (5 * n) for _ in range(5 * n)]
for i in range(5 * n):
    result[i][i] = 1
while t > 0:
    if t & 1:
        result = multiple_matrix(result, table)
    table = multiple_matrix(table)
    t >>= 1
print(result[5 * (s - 1)][5 * (e - 1)])
