# 1948 임계경로
# 플5 찍먹

from sys import stdin as s
from collections import deque

n = int(s.readline())
m = int(s.readline())
connection = [[] for _ in range(n + 1)]
connection1 = [[] for _ in range(n + 1)]
get_in = [0] * (n + 1)
for _ in range(m):
    x, y, d = map(int, s.readline().split())
    connection[x].append((y, d))
    connection1[y].append((x, d))
    get_in[y] += 1
init, fin = map(int, s.readline().split())
time = [0] * (n + 1)
start = deque()
start.append(init)
end = deque()
end.append(fin)

while start:
    now = start.popleft()
    for road in connection[now]:
        arrival = road[0]
        distance = road[1]
        get_in[arrival] -= 1
        time[arrival] = max(time[arrival], time[now] + distance)
        if get_in[arrival] == 0:
            start.append(arrival)
ans = 0
visited = [False] * (n + 1)
while end:
    now = end.popleft()
    for road in connection1[now]:
        arrival = road[0]
        distance = road[1]
        if time[arrival] + distance == time[now]:
            ans += 1
            if not visited[arrival]:
                end.append(arrival)
                visited[arrival] = True
print(time[fin])
print(ans)
