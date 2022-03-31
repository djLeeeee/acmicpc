from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


def dfs_inv(idx):
    for adj in graph[idx][::-1]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match_inv[adj] or dfs_inv(match_inv[adj]):
            match_inv[adj] = idx
            return 1
    return 0


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n):
    m, *ans = map(int, input().split())
    graph[i + 1] = ans
match = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    ans += dfs(i)
if ans == n:
    match_inv = [0] * (n + 1)
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs_inv(i)
    if match == match_inv:
        print(1)
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[match[i]] = i
        print(*result[1:])
    else:
        print('-1')
else:
    print('-1')
