# 11280 2-SAT - 3
# i | j 는 (~ i -> j) & (~j -> i) 과 동치 
from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
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


n, m = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[-x].append(y)
    graph[-y].append(x)
    graph_inv[x].append(-y)
    graph_inv[y].append(-x)
visited = defaultdict(bool)
checked = defaultdict(bool)
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
print(max(flag, 0))
