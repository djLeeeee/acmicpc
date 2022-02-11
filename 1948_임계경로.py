# 1948 임계경로
# 플5 찍먹

from sys import stdin as s
from collections import deque

n = int(s.readline())
m = int(s.readline())
connection = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, s.readline().split())
    connection[x].append(([y], d))
init, fin = map(int, s.readline().split())
start = deque(connection[init][:])
max_d = 0
while start:
    now, distance = start.popleft()
    for j in connection[now[-1]]:
        if j[0][-1] == fin:
            now = now[:]
            now.append(fin)
            if max_d < distance + j[1]:
                ans = [now]
                max_d = distance + j[1]
            elif max_d == distance + j[1]:
                ans.append(now)
        else:
            now = now[:]
            now.append(j[0][-1])
            start.append((now, distance + j[1]))
            if max_d < distance + j[1]:
                ans = []
print(max_d)
road = set()
for path in ans:
    road.add((init, path[0]))
    for i in range(len(path) - 1):
        road.add((path[i], path[i + 1]))
print(len(road))