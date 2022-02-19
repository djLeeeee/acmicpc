from sys import stdin as s
from sys import setrecursionlimit as st
st(10 ** 6)

m, n = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = [[-1] * n for _ in range(m)]
result[-1][-1] = 1


def dfs(x, y):
    if result[x][y] >= 0:
        return result[x][y]
    result[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[x][y] > board[nx][ny]:
            result[x][y] += dfs(nx, ny)
    return result[x][y]


print(dfs(0, 0))
