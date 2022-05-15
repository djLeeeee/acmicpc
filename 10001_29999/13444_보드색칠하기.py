from sys import stdin, setrecursionlimit
from collections import defaultdict

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


n, m = map(int, input().split())
board = [input() for _ in range(n)]
node = 0
edge_r = 0
edge_c = 0
row = defaultdict(list)
col = defaultdict(list)
graph = defaultdict(list)
for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            node += 1
            if j + 1 < m and board[i][j + 1] == '#':
                edge_r += 1
                row[(i, j)].append(edge_r)
                row[(i, j + 1)].append(edge_r)
            if i + 1 < n and board[i + 1][j] == '#':
                edge_c += 1
                col[(i, j)].append(edge_c)
                col[(i + 1, j)].append(edge_c)
            if row[(i, j)] and col[(i, j)]:
                for r in row[(i, j)]:
                    graph[r] += col[(i, j)]
ans = node - edge_r - edge_c
match = [0] * (edge_c + 1)
for i in range(1, edge_r + 1):
    visited = [False] * (edge_c + 1)
    ans += dfs(i)
print(ans)
