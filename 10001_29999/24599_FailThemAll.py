from sys import stdin

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
    if scc[idx] or not flag:
        return
    scc[idx] = component
    if scc[-idx]:
        if scc[-idx] == component:
            flag = False
            return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


m, n = map(int, input().split())
graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    order = input().rstrip()
    node = []
    for i in range(n):
        if order[i] == 'T':
            node.append(i + 1)
        elif order[i] == 'F':
            node.append(-i - 1)
    l = len(node)
    for i in range(l - 1):
        for j in range(i + 1, l):
            graph[node[i]].append(-node[j])
            graph[node[j]].append(-node[i])
stack = []
visited = [False] * (2 * n + 1)
for i in range(1, n + 1):
    if not visited[-i]:
        dfs(-i)
    if not visited[i]:
        dfs(i)
scc = [0] * (2 * n + 1)
component = 0
flag = True
while stack and flag:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
if flag:
    ans = ''
    for j in range(1, n + 1):
        graph[j].append(-j)
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
            ans += 'F'
        else:
            ans += 'T'
            graph[-j].append(j)
            graph[j].pop()
    print(ans)
else:
    print(-1)
