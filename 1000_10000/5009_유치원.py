from sys import stdin

input = stdin.readline


def draw_or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def draw_edge(x, y):
    cx, cy = past[x], past[y]
    if (cx + 1) % 3 == cy:
        draw_or_edge(x, -y)
    elif (cx - 1) % 3 == cy:
        draw_or_edge(-x, y)
    else:
        draw_or_edge(x, y)
        draw_or_edge(-x, -y)


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
    if scc[idx]:
        return
    scc[idx] = component
    if scc[-idx] == scc[idx]:
        flag = False
        return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n = int(input())
past = [0] * (n + 1)
rank = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    c, *r = map(int, input().split())
    past[i] = c
    rank[i] += r
start = 0
end = n - 1
while start <= end:
    middle = (start + end) // 2
    graph = [[] for _ in range(2 * n + 1)]
    for i in range(1, n + 1):
        for j in range(middle + 1, n):
            draw_edge(i, rank[i][j])
    stack = []
    visited = [False] * (2 * n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    scc = [0] * (2 * n + 1)
    component = 0
    flag = True
    while stack and flag:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    if flag:
        ans = middle
        end = middle - 1
    else:
        start = middle + 1
print(ans)
