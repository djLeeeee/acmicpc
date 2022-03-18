from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 5)


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if not visited[idx]:
        return
    visited[idx] = False
    for adj in graph_inv[idx]:
        if visited[adj]:
            dfs_inv(adj)
    component.append(idx)


n, m = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_inv[y].append(x)
scc = []
visited = [False] * (n + 1)
stack = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
while stack:
    now = stack.pop()
    if visited[now]:
        component = []
        dfs_inv(now)
        component.sort()
        scc.append(component)
scc.sort()
print(len(scc))
for c in scc:
    print(*c, -1)
