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
    if check[idx] or not visited[idx]:
        return
    check[idx] = True
    for adj in graph_inv[idx]:
        if not check[adj]:
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
for i in range(1, n + 1):
    stack = []
    if not visited[i]:
        dfs(i)
        check = [False] * (n + 1)
        while stack:
            component = []
            now = stack.pop()
            if not check[now]:
                dfs_inv(now)
                if component:
                    component.sort()
                    scc.append(component)
scc.sort()
print(len(scc))
for c in scc:
    print(*c, -1)
