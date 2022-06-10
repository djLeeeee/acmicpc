from sys import stdin

input = stdin.readline


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
graph = [[] for _ in range(n + 1)]
relation = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    line = input()
    for j in range(n):
        if line[j] == '1':
            relation[i].append(j + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    point = [i]
    while point:
        now = point.pop()
        for nei in relation[now]:
            if not visited[nei]:
                visited[nei] = True
                point.append(nei)
                graph[i].append(nei)
match = [0] * (n + 1)
ans = n
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    ans -= dfs(i)
print(ans)
