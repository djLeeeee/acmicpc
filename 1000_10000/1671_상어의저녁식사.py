from sys import stdin

input = stdin.readline


def check(x, y):
    if shark[x][0] <= shark[y][0] and shark[x][1] <= shark[y][1] and shark[x][2] <= shark[y][2]:
        return 1
    return 0


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
shark = [0] + [tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if check(i, j):
            graph[i].append(j)
            graph[i].append(j + n)
        elif check(j, i):
            graph[j].append(i)
            graph[j].append(i + n)
ans = n
match = [0] * (2 * n + 1)
for i in range(1, n + 1):
    visited = [False] * (2 * n + 1)
    ans -= dfs(i)
print(ans)
