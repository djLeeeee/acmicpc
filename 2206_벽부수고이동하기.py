# 2206 벽 부수고 이동하기
# BFS와 비슷하나, 오는 길에 벽을 뚫고 왔는지 여부를 체크하는 변수 ([x, y, bool])
# + 해당 지점을 올 때 벽을 뚫었는지 저장할 리스트 crashed 를 추가
# 벽을 뚫고 왔다면 해당 지점은 이미 방문을 한 것이니 논리문을 좀 더 간결화 할 수 있었을 듯.
# 지금은 귀찮으니 나중에 해보자.

from sys import stdin as s

n, m = map(int, s.readline().split())
board = [ ]
for _ in range(n):
    board.append(list(map(int, s.readline().strip())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
starts = [[0, 0, False]]
visited = [[False] * m for _ in range(n)]
crashed = [[False] * m for _ in range(n)]
visited[0][0] = True
ans = 1
while (not visited[-1][-1]) and starts:
    new_starts = []
    ans += 1
    for start in starts:
        x = start[0]
        y = start[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if start[2] and board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    crashed[nx][ny] = True
                    new_starts.append([nx, ny, True])
                elif not start[2]:
                    if board[nx][ny] == 0:
                        if crashed[nx][ny] and visited[nx][ny]:
                            crashed[nx][ny] = False
                            new_starts.append([nx, ny, False])
                        elif not visited[nx][ny]:
                            visited[nx][ny] = True
                            new_starts.append([nx, ny, False])
                    else:
                        if not crashed[nx][ny]:
                            crashed[nx][ny] = True
                            new_starts.append([nx, ny, True])
                            visited[nx][ny] = True
    starts = new_starts
if visited[-1][-1]:
    print(ans)
else:
    print(-1)