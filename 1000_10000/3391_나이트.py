from sys import stdin
from sys import setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def dfs(x):
    for adj in graph[x]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = x
            return 1
    return 0


n, m = map(int, input().split())
cant = set(tuple(map(int, input().split())) for _ in range(m))
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
graph = {}
ans = n * n - m
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i, j) not in cant and (i - j) % 2:
            graph[(i - 1) * n + j - 1] = []
            for d in range(8):
                ni = i + dx[d]
                nj = j + dy[d]
                if 1 <= ni <= n and 1 <= nj <= n and (ni, nj) not in cant:
                    graph[(i - 1) * n + j - 1].append((ni - 1) * n + nj - 1)
match = [-1] * (n * n)
for s in range(n * n):
    if s in graph:
        visited = [False] * (n * n)
        ans -= dfs(s)
print(ans)
