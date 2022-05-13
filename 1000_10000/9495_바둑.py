from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
board = [list(input().strip()) for _ in range(n)]
blank = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            blank += 1
            board[i][j] = blank
graph = [[] for _ in range(blank + 1)]
white = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'o':
            white += 1
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and type(board[ni][nj]) == int:
                    graph[board[ni][nj]].append(white)
ans = white + blank
match = [0] * (white + 1)
for i in range(1, blank + 1):
    visited = [False] * (white + 1)
    ans -= dfs(i)
print(ans)
