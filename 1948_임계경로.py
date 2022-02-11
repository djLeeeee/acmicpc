# 1948 임계경로
# 플5 찍먹

from sys import stdin as s
from collections import deque

n = int(s.readline())
m = int(s.readline())
connection = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, s.readline().split())
    connection[x].append([d, y])
init, fin = map(int, s.readline().split())
time = [0] * (n + 1)
start = deque(connection[init])
while start:
    now = start.popleft()
    for j in connection[now[-1]]:
        if j[-1] == fin:
            x = now[:]
            x.append(fin)
            if time[fin] < x[0] + j[0]:
                ans = [x]
                time[fin] = x[0] + j[0]
            elif time[fin] == x[0] + j[0]:
                ans.append(x)
        else:
            x = now[:]
            x.append(j[-1])
            if time[j[-1]] <= x[0] + j[0]:
                time[j[-1]] = x[0] + j[0]
                x[0] += j[0]
                start.append(x)
            if time[fin] < x[0] + j[0]:
                ans = []
print(time[fin])
road = set()
for path in ans:
    road.add((init, path[1]))
    for i in range(1, len(path) - 1):
        road.add((path[i], path[i + 1]))
print(len(road))
