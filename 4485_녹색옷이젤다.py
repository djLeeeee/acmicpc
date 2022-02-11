# 4485_녹색 옷 입은 애가 젤다지?
# 다익스트라 문제
# 1261 알고스팟 문제에서 각 칸의 비용이 0, 1 말고도 있는 경우임
# 같은 방법으로 진행하자.

from sys import stdin as s
from math import inf
import heapq

input = s.readline
t = 0
while True:
    n = int(input())
    if n == 0:
        break
    t += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    labyrinth = []
    for i in range(n):
        labyrinth.append(list(map(int, input().split())))
    d = [[inf] * n for _ in range(n)]
    d[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heap:
        cost, x, y = heapq.heappop(heap)
        if cost > d[x][y]:
            continue
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] > cost + labyrinth[nx][ny]:
                d[nx][ny] = cost + labyrinth[nx][ny]
                heapq.heappush(heap, (d[nx][ny], nx, ny))
    print(f'Problem {t}: {d[-1][-1] + labyrinth[0][0]}')
