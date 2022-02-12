# 16236 아기 상어
# BFS 탐색 + 문제 조건에 맞게 구현하기
# 재밌는 문제였다

from sys import stdin as s

n = int(s.readline())
shark_size = 2
space = [ ]
find_shark = False
for i in range(n):
    a = list(map(int, s.readline().split()))
    space.append(a)
    if not find_shark:
        if a.count(9):
            position = [i, a.index(9)]
            find_shark = True
            space[-1][position[1]] = 0

def find_food(position):
    x = position[0]
    y = position[1]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    start = [position]
    time = 0
    while start:
        time += 1
        new_start = [ ]
        can_eat = [ ]
        for i in start:
            x = i[0]
            y = i[1]
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n and space[nx][ny] <= shark_size and not visited[nx][ny]:
                    if 0 < space[nx][ny] < shark_size:
                        can_eat.append([nx, ny])
                    visited[nx][ny] = True
                    new_start.append([nx, ny])
        if can_eat:
            can_eat.sort()
            space[can_eat[0][0]][can_eat[0][1]] = 0
            return can_eat[0] + [time]
        start = new_start[:]
    return False

result = 0
eat = 0
while True:
    food = find_food(position)
    if food:
        result += food[2]
        position = food[:2]
        eat += 1
        if eat == shark_size:
            shark_size += 1
            eat = 0
    else:
        print(result)
        exit(0)