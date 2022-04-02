from sys import stdin

input = stdin.readline


def to_idx(my_str):
    if my_str[1] == 'h':
        return int(my_str[:-1]) + 1
    return -(int(my_str[:-1]) + 1)


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


def seat():
    ans = ''
    for idx in range(2, n + 1):
        if scc[idx] > scc[-idx]:
            ans += str(idx - 1) + 'h '
        else:
            ans += str(idx - 1) + 'w '
    return ans[:-1]


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    graph = [[] for _ in range(2 * n + 1)]
    graph[1].append(-1)
    for _ in range(m):
        x, y = map(to_idx, input().strip().split())
        graph[-x].append(y)
        graph[-y].append(x)
    stack = []
    visited = [False] * (2 * n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    scc = [0] * (2 * n + 1)
    flag = True
    component = 0
    while stack and flag:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    if flag:
        print(seat())
    else:
        print("bad luck")
