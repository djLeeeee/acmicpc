# 1167 트리의 지름
# 시작점 아무데나 잡고
# 최대 거리가 나오는 점이 지름의 끝 점 중 하나가 된다
# 그 점에서 다시 최대 거리 점 찾으면 끝

"""
# BFS 사용 풀이 (비추)
from sys import stdin as s

input = s.readline

n = int(input())
connection = [[] for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    node = a[0]
    p = 1
    while a[p] != -1:
        connection[node].append((a[p], a[p + 1]))
        p += 2
dist = [0] * (n + 1)
dist[1] = 0
start = [1]
while start:
    new_start = []
    for now in start:
        for v, c in connection[now]:
            if not dist[v] and v != 1:
                dist[v] = dist[now] + c
                new_start.append(v)
    start = new_start
x = dist.index(max(dist))
start = [x]
dist = [0] * (n + 1)
dist[x] = 0
while start:
    new_start = []
    for now in start:
        for v, c in connection[now]:
            if not dist[v] and v != x:
                dist[v] = dist[now] + c
                new_start.append(v)
    start = new_start
print(max(dist))
"""

# DFS 사용 풀이(강추)
from sys import stdin as s

input = s.readline

n = int(input())
connection = [[] for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    node = a[0]
    p = 1
    while a[p] != -1:
        connection[node].append((a[p], a[p + 1]))
        p += 2
visited = [False] * (n + 1)


def dfs(start, distance):
    visited[start] = True
    end, r = start, distance
    for now, cost in connection[start]:
        if not visited[now]:
            ver, dist = dfs(now, distance + cost)
            if dist > r:
                end = ver
                r = dist
    return end, r


s, _ = dfs(1, 0)
visited = [False] * (n + 1)
_, ans = dfs(s, 0)
print(ans)

