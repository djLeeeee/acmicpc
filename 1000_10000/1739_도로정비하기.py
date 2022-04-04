from sys import stdin

input = stdin.readline


def draw_edge(a, b, c, d):
    graph[-a].append(b)
    graph[-a].append(c)
    graph[-d].append(b)
    graph[-d].append(c)
    graph[-b].append(a)
    graph[-b].append(d)
    graph[-c].append(a)
    graph[-c].append(d)


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
    if scc[idx] == scc[-idx]:
        flag = False
        return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(2 * n + 2 * m + 1)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        y1 += n
        y2 += n
        if x1 == x2:
            if y1 > y2:
                graph[-x1].append(x1)
            elif y1 < y2:
                graph[x1].append(-x1)
        elif y1 == y2:
            if x1 > x2:
                graph[-y1].append(y1)
            elif x1 < x2:
                graph[y1].append(-y1)
        else:
            if x1 > x2:
                if y1 > y2:
                    draw_edge(x1, y1, x2, y2)
                elif y1 < y2:
                    draw_edge(-x1, y1, -x2, y2)
            elif x1 < x2:
                if y1 > y2:
                    draw_edge(x1, -y1, x2, -y2)
                elif y1 < y2:
                    draw_edge(-x1, -y1, -x2, -y2)
    stack = []
    visited = [False] * (2 * n + 2 * m + 1)
    for i in range(1, n + m + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    scc = [0] * (2 * n + 2 * m + 1)
    component = 0
    flag = True
    while stack and flag:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    if flag:
        print('Yes')
    else:
        print('No')