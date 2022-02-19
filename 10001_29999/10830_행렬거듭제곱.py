from sys import stdin as s


def matrix_multiple(first, second=None):
    if not second:
        second = first
    size = len(first)
    ans = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += first[i][k] * second[k][j]
            ans[i][j] %= 1000
    return ans


n, b = map(int, s.readline().split())
matrix = [list(map(int, s.readline().split())) for _ in range(n)]
ans = [[0] * n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1
x = matrix
while b > 0:
    if b & 1:
        ans = matrix_multiple(ans, x)
    x = matrix_multiple(x)
    b >>= 1
for line in ans:
    print(*line)
