from sys import stdin
from sys import setrecursionlimit as st
import heapq

st(10 ** 6)
input = stdin.readline


def find(t: int) -> int:
    if t == p[t]:
        return t
    p[t] = find(p[t])
    return p[t]


def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def dfs(a: int, b: int) -> None:
    board[a][b] = idx
    for d in range(4):
        na = a + dx[d]
        nb = b + dy[d]
        if 0 <= na < n and 0 <= nb < m and board[na][nb] == 1:
            dfs(na, nb)


n, m = map(int, input().split())
board = []
idx = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            idx += 1
            dfs(x, y)
p = list(range(idx + 1))
bridge = set()
for xx in range(n):
    for yy in range(m):
        if board[xx][yy]:
            for dd in range(4):
                nx, ny = xx, yy
                cost = 0
                nx += dx[dd]
                ny += dy[dd]
                while 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                    cost += 1
                    nx += dx[dd]
                    ny += dy[dd]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and cost > 1:
                    bridge.add((cost, board[xx][yy], board[nx][ny]))
bridge = list(bridge)
heapq.heapify(bridge)
edge = 0
total = 0
while edge < idx - 2 and bridge:
    c, init, fin = heapq.heappop(bridge)
    if find(init) != find(fin):
        union(init, fin)
        total += c
        edge += 1
if bridge:  # 같은 종류의 다리가 2개 씩 저장되어 있어, 섬을 다 이었다면 bridge 는 비어있지 않다
    print(total)
else:
    print('-1')
