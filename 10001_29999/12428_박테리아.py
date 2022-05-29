from sys import stdin
from collections import defaultdict

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


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
df = [1, -1]
for t in range(int(input())):
    room = 0
    n, m, k = map(int, input().split())
    building = []
    for _ in range(k):
        floor = [list(input().strip()) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if floor[i][j] == '.':
                    room += 1
                    floor[i][j] = room
                    point = [(i, j)]
                    while point:
                        x, y = point.pop()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < n and 0 <= ny < m and floor[nx][ny] == '.':
                                floor[nx][ny] = room
                                point.append((nx, ny))
                elif floor[i][j] == '#':
                    floor[i][j] = 0
        building.append(floor)
    graph = defaultdict(set)
    for f in range(0, k, 2):
        for i in range(n):
            for j in range(m):
                if building[f][i][j]:
                    for d in range(2):
                        nf = f + df[d]
                        if 0 <= nf < k and building[nf][i][j]:
                            graph[building[f][i][j]].add(building[nf][i][j])
    ans = room
    match = [0] * (room + 1)
    for room_idx in graph:
        visited = [False] * (room + 1)
        ans -= dfs(room_idx)
    print(f"Case #{t + 1}: {ans}")
