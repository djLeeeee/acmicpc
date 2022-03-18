# 10265 MT
from sys import stdin
from collections import defaultdict

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
    global component
    if check[idx]:
        return
    check[idx] = True
    for adj in graph_inv[idx]:
        if not check[adj]:
            dfs_inv(adj)
    component += 1
    scc[idx] = num


def dfs_scc(idx):
    if visited_scc[idx]:
        return 0
    visited_scc[idx] = True
    res = scc_size[idx]
    for adj in graph_scc[idx]:
        if not visited_scc[adj]:
            res += dfs_scc(adj)
    return res


def sol(array, limit):
    dp = [0] * (n + 1)
    dp[0] = 1
    for start, end in array:
        for x in range(limit - start, -1, -1):
            if dp[x]:
                dp[x + start:x + end + 1] = [1] * (end - start + 1)
    for res in range(limit, -1, -1):
        if dp[res]:
            return res


n, k = map(int, input().split())
graph = defaultdict(list)
graph_inv = defaultdict(list)
order = tuple(map(int, input().split()))
# graph[i] = [j] i가 가면 j가 감
for i in range(n):
    graph[i + 1].append(order[i])
    graph_inv[order[i]].append(i + 1)
stack = []
visited = [False] * (n + 1)
for j in range(1, n + 1):
    if not visited[j]:
        dfs(j)
check = [False] * (n + 1)
scc = [0] * (n + 1)
scc_size = [0]
num = 0
while stack:
    now = stack.pop()
    if not check[now]:
        component = 0
        num += 1
        dfs_inv(now)
        scc_size.append(component)
graph_scc = defaultdict(list)
deg_scc = [0] * (num + 1)
# deg 가 0인 애들부터 처리하는 게 좋다.
# 먼저 처리해야 하는 놈 = i가 가면 j가 갈때 j
for i in range(n):
    if scc[i + 1] != scc[order[i]]:
        graph_scc[scc[order[i]]].append(scc[i + 1])
        deg_scc[scc[i + 1]] += 1
leaves_scc = []
for j in range(1, num + 1):
    if deg_scc[j] == 0:
        leaves_scc.append(j)
visited_scc = [False] * (num + 1)
size_range = []
for leaf in leaves_scc:
    size_range.append((scc_size[leaf], dfs_scc(leaf)))
print(sol(size_range, k))
