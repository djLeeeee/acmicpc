from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 4)
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
    global flag
    checked[idx] = True
    component.add(idx)
    if -idx in component:
        flag -= 1
    for adj in graph_inv[idx]:
        if not checked[adj]:
            dfs_inv(adj)


while True:
    try:
        n, m = map(int, input().split())
    except ValueError:
        break
    graph = defaultdict(list)
    graph_inv = defaultdict(list)
    graph[-1].append(1)
    graph_inv[1].append(-1)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[-x].append(y)
        graph[-y].append(x)
        graph_inv[x].append(-y)
        graph_inv[y].append(-x)
    visited = [False] * (2 * n + 1)
    checked = [False] * (2 * n + 1)
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    flag = 1
    while stack and flag == 1:
        now = stack.pop()
        if not checked[now]:
            component = set()
            dfs_inv(now)
    if flag > 0:
        print('yes')
    else:
        print('no')
    del graph, graph_inv
