from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


def dfs(idx, limit):
    for adj in graph[idx]:
        if visited[adj] or graph[idx][adj] > limit:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj], limit):
            match[adj] = idx
            return 1
    return 0


n = int(input())
graph = defaultdict(dict)
for i in range(1, n + 1):
    a, ka, b, kb = map(int, input().split())
    graph[i][a] = ka
    graph[i][b] = kb
start = 0
end = 10 ** 6
result = -1
while start <= end:
    middle = (start + end) // 2
    match = defaultdict(int)
    flag = True
    for i in range(1, n + 1):
        visited = defaultdict(bool)
        if not dfs(i, middle):
            flag = False
            break
    if flag:
        result = middle
        end = middle - 1
    else:
        start = middle + 1
print(result)
