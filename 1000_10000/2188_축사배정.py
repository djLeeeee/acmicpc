# 2188 축사 배정 - 복습
from sys import stdin

input = stdin.readline


def dfs(x):
    for adj in graph[x]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = x
            return True
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    _, *k = list(map(int, input().split()))
    graph[i] = k
match = [0] * (m + 1)
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    dfs(i)
ans = 0
for idx in match:
    if idx:
        ans += 1
print(ans)
