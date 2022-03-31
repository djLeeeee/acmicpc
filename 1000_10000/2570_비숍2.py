from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
ln = 0
ld_board = [[0] * n for _ in range(n)]
rn = 0
rd_board = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    ld_board[x - 1][y - 1] = -1
    rd_board[x - 1][y - 1] = -1
for i in range(n):
    for j in range(n):
        if not ld_board[i][j]:
            ln += 1
            ii, jj = i, j
            while ii < n and jj < n and not ld_board[ii][jj]:
                ld_board[ii][jj] = ln
                ii += 1
                jj += 1
        if not rd_board[i][j]:
            rn += 1
            ii, jj = i, j
            while ii < n and jj >= 0 and not rd_board[ii][jj]:
                rd_board[ii][jj] = rn
                ii += 1
                jj -= 1
graph = [[] for _ in range(ln + 1)]
for i in range(n):
    for j in range(n):
        if ld_board[i][j] > 0:
            graph[ld_board[i][j]].append(rd_board[i][j])
match = [0] * (rn + 1)
ans = 0
for i in range(1, ln + 1):
    visited = [False] * (rn + 1)
    ans += dfs(i)
print(ans)
