from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
row = [[0] * m for _ in range(n)]
col = [[0] * m for _ in range(n)]
rn = 0
cn = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '*' and not row[i][j]:
            rn += 1
            jj = j
            while jj < m and board[i][jj] == '*':
                row[i][jj] = rn
                jj += 1
for j in range(m):
    for i in range(n):
        if board[i][j] == '*' and not col[i][j]:
            cn += 1
            ii = i
            while ii < n and board[ii][j] == '*':
                col[ii][j] = cn
                ii += 1
graph = [[] for _ in range(rn + 1)]
for i in range(n):
    for j in range(m):
        if row[i][j]:
            graph[row[i][j]].append(col[i][j])
ans = 0
match = [0] * (cn + 1)
for i in range(1, rn + 1):
    visited = [False] * (cn + 1)
    ans += dfs(i)
print(ans)
