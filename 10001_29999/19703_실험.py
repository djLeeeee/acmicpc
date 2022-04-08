from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


def draw_edge(x, y):
    graph[-y].append(x)
    graph[-x].append(y)


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
    if scc[-idx] == component:
        print('NIE')
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m, a, b = map(int, input().split())
group = defaultdict(list)
graph = defaultdict(list)
for _ in range(a):
    i, j = map(int, input().split())
    group[j].append(i)
gn = n + 1
for g in group.values():
    for k in range(len(g) - 1):
        draw_edge(-gn - k, gn + k + 1)
        draw_edge(-g[k], gn + k)
        draw_edge(-gn - k, -g[k + 1])
    draw_edge(-g[-1], gn + len(g) - 1)
    gn += len(g)
for _ in range(b):
    i, j = map(int, input().split())
    draw_edge(i, j)
stack = []
visited = defaultdict(bool)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = defaultdict(int)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print('TAK')
