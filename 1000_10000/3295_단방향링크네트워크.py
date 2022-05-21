from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    ans = 0
    match = [-1] * n
    for i in range(n):
        visited = [False] * n
        ans += dfs(i)
    print(ans)
