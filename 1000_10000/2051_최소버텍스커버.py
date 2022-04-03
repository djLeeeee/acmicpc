from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(x):
    for adj in graph[x]:
        if not visited[adj]:
            visited[adj] = True
            if not match[adj] or dfs(match[adj]):
                match[adj] = x
                check[x] = True
                return 1
    return 0


def coloring(idx):
    used_a[idx] = False
    for adj in graph[idx]:
        if match[adj] != idx:
            used_b[adj] = True
            if used_a[match[adj]]:
                coloring(match[adj])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    _, *k = map(int, input().split())
    graph[i] = k
match = [0] * (m + 1)
check = [False] * (n + 1)
ans = 0
for j in range(1, n + 1):
    visited = [False] * (m + 1)
    ans += dfs(j)
print(ans)
used_a = [True] * (n + 1)
used_b = [False] * (m + 1)
for i in range(1, n + 1):
    if not check[i]:
        coloring(i)
a = [i for i in range(1, n + 1) if used_a[i]]
b = [j for j in range(1, m + 1) if used_b[j]]
print(len(a), *a)
print(len(b), *b)
