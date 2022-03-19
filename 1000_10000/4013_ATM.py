# 4013 ATM
from sys import stdin, setrecursionlimit
from collections import defaultdict, deque

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
    scc[idx] = component
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)
        elif scc[idx] != scc[adj]:
            graph_scc[scc[adj]].append(scc[idx])
    component_cost[component] += cost[idx]


n, m = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_inv[y].append(x)
cost = [0] * (n + 1)
for i in range(1, n + 1):
    cost[i] = int(input())
start, _ = map(int, input().split())
scc = [0] * (n + 1)
visited = [False] * (n + 1)
stack = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
del graph
component = 0
component_cost = defaultdict(int)
graph_scc = defaultdict(list)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
del graph_inv
ans = 0
total_cost = [0] * (component + 1)
starts = deque([scc[start]])
total_cost[scc[start]] = component_cost[scc[start]]
while starts:
    now = starts.popleft()
    for adj_scc in graph_scc[now]:
        if total_cost[adj_scc] < total_cost[now] + component_cost[adj_scc]:
            total_cost[adj_scc] = total_cost[now] + component_cost[adj_scc]
            starts.append(adj_scc)
for r in map(int, input().split()):
    ans = max(ans, total_cost[scc[r]])
print(ans)
