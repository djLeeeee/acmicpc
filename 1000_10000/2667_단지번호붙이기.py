# 2667 단지번호붙이기
# DFS 재밌음

from sys import stdin as s

n = int(s.readline())
town = []
for _ in range(n):
    town.append([int(i) for i in s.readline().strip()])

result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
ans = [ ]
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            result += 1
            nums = 1
            visited = [(i, j)]
            town[i][j] = 0
            while visited:
                a = visited.pop()
                for k in range(4):
                    nx = a[0] + dx[k]
                    ny = a[1] + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and town[nx][ny] == 1:
                        town[nx][ny] = 0
                        nums += 1
                        visited.append((nx, ny))
            ans.append(nums)
print(result)
ans.sort()
print(*ans, sep = '\n')