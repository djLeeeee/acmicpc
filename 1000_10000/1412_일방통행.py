from sys import stdin

input = stdin.readline


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if scc[idx]:
        return
    scc[idx] = component
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)


n = int(input())
board = [input().strip() for _ in range(n)]
graph = [[] for _ in range(n)]
graph_inv = [[] for _ in range(n)]
for s in range(n - 1):
    for e in range(s + 1, n):
        if board[s][e] == 'Y' and board[e][s] == 'N':
            graph[s].append(e)
            graph_inv[e].append(s)
        elif board[s][e] == 'N' and board[e][s] == 'Y':
            graph[e].append(s)
            graph_inv[s].append(e)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(i)
component = 0
scc = [0] * n
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
if component == n:
    print('YES')
else:
    print('NO')
