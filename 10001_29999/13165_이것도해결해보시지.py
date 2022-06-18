from sys import stdin
from random import randint

input = stdin.readline


def test(idx):
    for _ in range(20):
        v = [randint(0, 1) for _ in range(n)]
        v1 = [0] * n
        v2 = [0] * n
        v3 = [0] * n
        for i in range(n):
            for j in range(n):
                v1[i] += board[i][idx + n + j] * v[j]
        for i in range(n):
            for j in range(n):
                v2[i] += board[i][idx + j] * v1[j]
        for i in range(n):
            for j in range(n):
                v3[i] += board[i][idx + 2 * n + j] * v[j]
            if v2[i] != v3[i]:
                return False
    return True


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
p = 0
ans = 0
while p + 3 * n <= m:
    if test(p):
        ans += 3 * n * n
        p += 3 * n
    else:
        p += 1
print(ans)
