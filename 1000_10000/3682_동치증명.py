from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


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
        elif scc[adj] != scc[idx]:
            deg_scc_in[scc[idx]] = 1
            deg_scc_out[scc[adj]] = 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        continue
    if m == 0:
        print(n)
        continue
    graph = [[] for _ in range(n + 1)]
    graph_inv = [[] for _ in range(n + 1)]
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
    deg_scc_in = defaultdict(int)
    deg_scc_out = defaultdict(int)
    while stack:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    del graph_inv
    if component == 1:
        print(0)
    else:
        print(component - min(sum(deg_scc_in.values()), sum(deg_scc_out.values())))
