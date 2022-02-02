# 7569 3차원 토마토 문제
# 2차원 토마토에 리스트 좀만 바꿔주면 될듯?

from sys import stdin

r = stdin.readline
m, n, h = map(int, r().split())
tomato = []
start = []
for i in range(h):
    floor = [ ]
    for j in range(n):
        a = list(map(int, r().split()))
        for k in range(m):
            if a[k] == 1:
                start.append([i, j, k])
        floor.append(a)
    tomato.append(floor)
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
day = 0
while True:
    new_start = []
    for i in start:
        x = i[0]
        y = i[1]
        z = i[2]
        for j in range(6):
            nx = x + dx[j]
            ny = y + dy[j]
            nz = z + dz[j]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = 1
                    new_start.append([nx, ny, nz])
    if new_start == []:
        break
    start = new_start
    day += 1
for tx in range(h):
    for ty in range(n):
        for tz in range(m):
            if tomato[tx][ty][tz] == 0:
                print(-1)
                exit(0)
                
print(day)