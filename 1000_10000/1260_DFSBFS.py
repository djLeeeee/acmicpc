from sys import stdin as s
from collections import deque


def DFS(start):  # 깊이 우선 (2)
    result = []
    need_visit = [start]
    while need_visit:
        now = need_visit.pop()
        if now not in result:
            result.append(now)
            for i in connection[now][::-1]:
                need_visit.append(i)
    return result


def BFS(start):  # 너비 우선 (2)
    result = []
    need_visit = deque([start])
    while need_visit:
        now = need_visit.popleft()
        if now in result:
            continue
        result.append(now)
        for can_go in connection[now]:
            if can_go not in result:
                need_visit.append(can_go)
    return result


N, M, V = map(int, s.readline().split())  # 변수 받기
connection = [[] for i in range(N + 1)]  # line graph 생성 (2)
for _ in range(M):
    x, y = map(int, s.readline().split())
    connection[x].append(y)
    connection[y].append(x)

for i in range(N + 1):
    connection[i].sort()

print(*DFS(V))
print(*BFS(V))
