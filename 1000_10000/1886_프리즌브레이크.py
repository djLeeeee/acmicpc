from sys import stdin
from collections import defaultdict

input = stdin.readline


def update(x, y):
    idx = board[x][y]
    checked = [False] * (pn + 1)
    point = [(x, y)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    day = 0
    while point:
        new = []
        day += 1
        for x, y in point:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] > 0 and not checked[board[nx][ny]]:
                    checked[board[nx][ny]] = True
                    new.append((nx, ny))
                    for ex in range(day, 201):
                        graph[board[nx][ny]].append((ex, -idx))
        point = new


def sol(limit):

    def dfs(idx):
        for t in graph[idx]:
            if t[0] <= limit and not visited[t]:
                visited[t] = True
                if not match[t] or dfs(match[t]):
                    match[t] = idx
                    return 1
        return 0

    match = defaultdict(int)
    for ii in range(1, pn + 1):
        visited = defaultdict(bool)
        if not dfs(ii):
            return 0
    return 1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
gn = 0
pn = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            gn += 1
            board[i][j] = -gn
        elif board[i][j] == '.':
            pn += 1
            board[i][j] = pn
        else:
            board[i][j] = 0
graph = [[] for _ in range(pn + 1)]
for i in range(1, m - 1):
    if board[0][i]:
        update(0, i)
    if board[-1][i]:
        update(n - 1, i)
for i in range(1, n - 1):
    if board[i][0]:
        update(i, 0)
    if board[i][-1]:
        update(i, m - 1)
ans = 'impossible'
left = 1
right = 200
while left <= right:
    mid = (left + right) // 2
    if sol(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
