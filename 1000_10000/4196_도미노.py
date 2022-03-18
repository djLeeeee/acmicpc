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
    if check[idx]:
        return
    check[idx] = True
    for adj in graph_inv[idx]:
        if not check[adj]:
            dfs_inv(adj)
    scc[idx] = num


for t in range(int(input())):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    graph_inv = defaultdict(list)
    edge = [tuple(map(int, input().split())) for _ in range(m)]
    for x, y in edge:
        graph[x].append(y)
        graph_inv[y].append(x)
    visited = [False] * (n + 1)
    scc = [0] * (n + 1)
    num = 0
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    check = [False] * (n + 1)
    while stack:
        now = stack.pop()
        if not check[now]:
            num += 1
            dfs_inv(now)
    child = set()
    for x, y in edge:
        if scc[x] != scc[y]:
            child.add(scc[y])
    print(num - len(child))
