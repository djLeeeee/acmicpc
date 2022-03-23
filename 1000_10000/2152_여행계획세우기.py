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
    if scc[idx]:
        return
    scc[idx] = component
    component_num[component] += 1
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)
        elif scc[adj] != scc[idx]:
            graph_scc[scc[adj]].add(scc[idx])


def dfs_scc(idx):
    for adj in graph_scc[idx]:
        if dp_scc[adj] < dp_scc[idx] + component_num[adj]:
            dp_scc[adj] = dp_scc[idx] + component_num[adj]
            dfs_scc(adj)


n, m, s, e = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_inv[y].append(x)
stack = []
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
del graph
scc = [0] * (n + 1)
component = 0
graph_scc = defaultdict(set)
component_num = defaultdict(int)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
del graph_inv
dp_scc = [0] * (component + 1)
dp_scc[scc[s]] = component_num[scc[s]]
dfs_scc(scc[s])
print(dp_scc[scc[e]])
