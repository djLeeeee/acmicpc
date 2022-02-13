# import sys
# sys.setrecursionlimit(10 ** 6)
# p = sys.stdin.readline

# def gogogo(x, y, M, N, ans):
#     if 0 <= x < M and 0 <= y < N:
#         if miroxy[y][x] == 1 and zeros[y][x] > ans:
#             zeros[y][x] = ans
#             if y == N - 1 and x == M - 1:
#                 return ans
#             miroxy[y][x] == 0
#             ans += 1
#             gogogo(x-1, y, M, N, ans)
#             gogogo(x+1, y, M, N, ans)
#             gogogo(x, y-1, M, N, ans)
#             gogogo(x, y+1, M, N, ans)

# N, M=map(int, p().split())
# miroxy = [ ]
# for _ in range(N):
#     a = str(p())
#     miroxy.append([int(a[i]) for i in range(M)])
# zeros=[[M * N] * M for i in range(N)]
# gogogo(0, 0, M, N, 1)
# print(zeros[N - 1][M - 1])

from sys import stdin

r = stdin.readline

n, m = map(int, r().split())
labyrinth = [ ]
for _ in range(n):
    labyrinth.append([int(i) for i in r().strip()])
start = [[0, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 1
while labyrinth[-1][-1] == 1:
    new_start = [ ]
    for i in start:
        x = i[0]
        y = i[1]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                if labyrinth[nx][ny] == 1:
                    new_start.append([nx, ny])
                    labyrinth[nx][ny] = 0
    day += 1
    start = new_start
print(day)
