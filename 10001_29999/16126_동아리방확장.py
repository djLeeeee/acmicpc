from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def sol():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    bn, wn = 0, 0
    for i in range(n):
        for j in range(m):
            if (i - j) % 2:
                if board[i][j] == 2:
                    bn += 2
                    board[i][j] = -bn
                elif board[i][j] == 3:
                    bn += 1
                    board[i][j] = bn
                elif board[i][j] == 4:
                    board[i][j] = 0
                else:
                    print("HOMELESS")
                    return
            else:
                if board[i][j] == 2:
                    wn += 2
                    board[i][j] = -wn
                elif board[i][j] == 3:
                    wn += 1
                    board[i][j] = wn
                elif board[i][j] == 4:
                    board[i][j] = 0
                else:
                    print("HOMELESS")
                    return
    if bn != wn:
        print("HOMELESS")
        return
    graph = [[] for _ in range(bn + 1)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(n):
        for y in range(m):
            if (x - y) % 2 and board[x][y]:
                now = board[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                        neighbor = board[nx][ny]
                        if now > 0:
                            if neighbor > 0:
                                graph[now].append(neighbor)
                            else:
                                graph[now].append(-neighbor)
                                graph[now].append(-neighbor - 1)
                        else:
                            if neighbor > 0:
                                graph[-now - 1].append(neighbor)
                                graph[-now].append(neighbor)

    def dfs(idx):
        for adj in graph[idx]:
            if not visited[adj]:
                visited[adj] = True
                if not match[adj] or dfs(match[adj]):
                    match[adj] = idx
                    return 1
        return 0

    match = [0] * (wn + 1)
    for i in range(1, bn + 1):
        visited = [False] * (wn + 1)
        if not dfs(i):
            print("HOMELESS")
            return
    print("HAPPY")
    return


sol()
