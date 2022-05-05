from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 5)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
ans = n
match = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    ans -= dfs(i)
print(ans)
