from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 4)


def or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def check(p1, p2):
    x1, y1, x2, y2 = p1
    x3, y3, x4, y4 = p2
    if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
        return False
    return True


def new_area(x):
    x1, y1, x2, y2 = map(int, input().split())
    group.append((x1, y1, x2, y2, x))
    for x3, y3, x4, y4, k in ground:
        if check((x3, y3, x4, y4), (x1, y1, x2, y2)):
            or_edge(k, x)


def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for adj in graph[x]:
        if not visited[adj]:
            dfs(adj)
    stack.append(x)


def dfs_inv(x):
    if scc[x]:
        return
    scc[x] = component
    if scc[x] == scc[-x]:
        print('NO')
        exit()
    for adj in graph[-x]:
        if not scc[-adj]:
            dfs_inv(-adj)


n = int(input())
graph = defaultdict(list)
ground = []
idx = 0
for _ in range(n):
    m = int(input())
    group = []
    for i in range(1, m):
        or_edge(-(idx + i), idx + m + i)
        or_edge(-(idx + m + i), -(idx + i + 1))
        or_edge(-(idx + m + i), idx + m + i + 1)
        new_area(idx + i)
    or_edge(-(idx + m), idx + 2 * m)
    new_area(idx + m)
    ground += group
    idx += 2 * m
stack = []
visited = defaultdict(bool)
for i in range(1, idx + 1):
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
print('YES')
