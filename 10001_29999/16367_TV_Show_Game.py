from collections import defaultdict
from sys import stdin, setrecursionlimit

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
    result = ''
    for ii in range(1, nn + 1):
        if array[ii] == array[-ii]:
            return -1
        if array[ii] < array[-ii]:
            result += 'B'
        else:
            result += 'R'
    return result


n, m = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    a = list(input().strip().split())
    order = [0, 0, 0]
    for i in range(3):
        if a[2 * i + 1] == 'R':
            order[i] = int(a[2 * i])
        else:
            order[i] = -int(a[2 * i])
    for i in range(3):
        for j in range(3):
            if i != j:
                graph[-order[i]].append(order[j])
                graph[-order[j]].append(order[i])
                graph_inv[order[i]].append(-order[j])
                graph_inv[order[j]].append(-order[i])
visited = [False] * (2 * n + 1)
stack = []
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
print(sol(scc))
