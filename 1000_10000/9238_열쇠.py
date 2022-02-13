# 9238 열쇠

from sys import stdin as s

t = int(s.readline())
for _ in range(t):
    m, n = map(int, s.readline().split())
    start = []
    visited = [[False] * n for _ in range(m)]
    board = []
    ans = 0
    new_key = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    a = list(s.readline().strip())
    for i in range(n):
        if a[i] == '.':
            start.append((0, i))
        elif a[i] == '$':
            ans += 1
            a[i] = '.'
            start.append((0, i))
        elif 'a' <= a[i] <= 'z':
            new_key.append(a[i])
            a[i] = '.'
            start.append((0, i))
    board.append(a)

    for j in range(1, m - 1):
        b = list(s.readline().strip())
        if b[0] == '.':
            start.append((j, 0))
        elif b[0] == '$':
            ans += 1
            b[0] = '.'
            start.append((j, 0))
        elif 'a' <= b[0] <= 'z':
            new_key.append(b[0])
            b[0] = '.'
            start.append((j, 0))
        if b[-1] == '.':
            start.append((j, n - 1))
        elif b[-1] == '$':
            ans += 1
            b[-1] = '.'
            start.append((j, n - 1))
        elif 'a' <= b[-1] <= 'z':
            new_key.append(b[-1])
            b[-1] = '.'
            start.append((j, n - 1))
        board.append(b)

    c = list(s.readline().strip())
    for k in range(n):
        if c[k] == '.':
            start.append((m - 1, k))
        elif c[k] == '$':
            ans += 1
            c[k] = '.'
            start.append((m - 1, k))
        elif 'a' <= c[k] <= 'z':
            new_key.append(c[k])
            c[k] = '.'
            start.append((m - 1, k))
    board.append(c)

    key = set(s.readline().strip())
    if key == {'0'}:
        key = set()
    key.update(new_key)
    fail_to_open = {}
    for i in range(n):
        if 'A' <= board[0][i] <= 'Z':
            if board[0][i].lower() in key:
                board[0][i] = '.'
                start.append((0, i))
            else:
                if fail_to_open.get(board[0][i], 0) == 0:
                    fail_to_open[board[0][i]] = [(0, i)]
                else:
                    fail_to_open[board[0][i]].append((0, i))
        if 'A' <= board[-1][i] <= 'Z':
            if board[-1][i].lower() in key:
                board[-1][i] = '.'
                start.append((m - 1, i))
            else:
                if fail_to_open.get(board[-1][i], 0) == 0:
                    fail_to_open[board[-1][i]] = [(m - 1, i)]
                else:
                    fail_to_open[board[-1][i]].append((m - 1, i))

    for j in range(1, m - 1):
        if 'A' <= board[j][0] <= 'Z':
            if board[j][0].lower() in key:
                board[j][0] = '.'
                start.append((j, 0))
            else:
                if fail_to_open.get(board[j][0], 0) == 0:
                    fail_to_open[board[j][0]] = [(j, 0)]
                else:
                    fail_to_open[board[j][0]].append((j, 0))
        if 'A' <= board[j][-1] <= 'Z':
            if board[j][-1].lower() in key:
                board[j][-1] = '.'
                start.append((j, n - 1))
            else:
                if fail_to_open.get(board[j][-1], 0) == 0:
                    fail_to_open[board[j][-1]] = [(j, n - 1)]
                else:
                    fail_to_open[board[j][-1]].append((j, n - 1))

    for st in start:
        visited[st[0]][st[1]] = True

    while start:
        new_start = []
        for now in start:
            x, y = now
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if board[nx][ny] == '.':
                        new_start.append((nx, ny))
                        visited[nx][ny] = True
                    elif board[nx][ny] == '$':
                        ans += 1
                        board[nx][ny] = '.'
                        new_start.append((nx, ny))
                    elif board[nx][ny] == '*':
                        visited[nx][ny] = True
                    else:
                        if 'A' <= board[nx][ny] <= 'Z':
                            if board[nx][ny].lower() in key:
                                board[nx][ny] = '.'
                                new_start.append((nx, ny))
                            else:
                                if fail_to_open.get(board[nx][ny], 0) == 0:
                                    fail_to_open[board[nx][ny]] = [(nx, ny)]
                                else:
                                    fail_to_open[board[nx][ny]].append((nx, ny))
                        else:
                            key.add(board[nx][ny])
                            new_start.append((nx, ny))
                            if fail_to_open.get(board[nx][ny].upper(), 0) != 0:
                                for pq in fail_to_open[board[nx][ny].upper()]:
                                    new_start.append((pq[0], pq[1]))
                                del fail_to_open[board[nx][ny].upper()]
                            board[nx][ny] = '.'
        start = new_start[:]
    print(ans)
