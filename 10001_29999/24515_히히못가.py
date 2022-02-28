# 24515 히히 못가
# dfs 로 영역 번호 부여하고, 다익스트라 진행
# 재밌긴 했는데, 시간 초과날 땐 좀 많이 짜증났다 ㅋ

from sys import setrecursionlimit as st
from sys import stdin as s
import heapq

input = s.readline

st(10 ** 6)

INF = int(1e9)
n = int(input())
board = [[0] * 2 + [2] * n, [0] + list(input().strip()) + [2]]
for _ in range(n - 2):
    board.append([1] + list(input().strip()) + [2])
board.append([1] + list(input().strip()) + [0])
board.append([1] * n + [0] * 2)
board[1][1] = 0
board[-2][-2] = 0
dxx = [1, -1, 0, 0]
dyy = [0, 0, 1, -1]
cost = {0: 0, 1: 0, 2: 0}


def dfs(xx, yy):
    global area
    board[xx][yy] = idx
    area += 1
    for dd in range(4):
        nxx = xx + dxx[dd]
        nyy = yy + dyy[dd]
        if board[nxx][nyy] == check:
            dfs(nxx, nyy)


idx = 2
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 'A' <= str(board[i][j]) <= 'Z':
            idx += 1
            check = board[i][j]
            area = 0
            dfs(i, j)
            cost[idx] = area
dx = [1, 1, 1, 0, -1]
dy = [1, 0, -1, 1, 1]
connection = {}
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if board[x][y]:
            for d in range(5):
                nx = x + dx[d]
                ny = y + dy[d]
                if board[nx][ny] and board[x][y] != board[nx][ny]:
                    if connection.get(board[x][y]):
                        connection[board[x][y]].add(board[nx][ny])
                    else:
                        connection[board[x][y]] = {board[nx][ny]}
                    if connection.get(board[nx][ny]):
                        connection[board[nx][ny]].add(board[x][y])
                    else:
                        connection[board[nx][ny]] = {board[x][y]}
dist = {i: INF for i in connection.keys()}
dist[1] = 0
start = []
heapq.heappush(start, (0, 1))
while start:
    distance, now = heapq.heappop(start)
    if dist[now] < distance:
        continue
    for can_go in connection[now]:
        if dist[can_go] > distance + cost[can_go]:
            dist[can_go] = distance + cost[can_go]
            heapq.heappush(start, (dist[can_go], can_go))
print(dist[2])
