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
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)


def sol(array):
    nn = len(array) // 2
    result = []
    for ii in range(1, nn + 1):
        if array[ii] == array[-ii]:
            return 0
        if array[ii] < array[-ii]:
            result.append(0)
        else:
            result.append(1)
    return result


n, m = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[-x].append(y)
    graph[-y].append(x)
    graph_inv[x].append(-y)
    graph_inv[y].append(-x)
stack = []
visited = [False] * (2 * n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (2 * n + 1)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
ans = sol(scc)
if ans:
    print(1)
    print(*ans)
else:
    print(0)
