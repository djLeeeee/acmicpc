from sys import stdin as s

r, c, m = map(int, s.readline().split())
board = [[0] * (c + 1) for _ in range(r + 1)]
shark = {}
for shark_id in range(1, m + 1):
    x, y, speed, direction, mass = map(int, s.readline().split())
    dx, dy = 0, 0
    if direction == 1:
        dx = -speed
    elif direction == 2:
        dx = speed
    elif direction == 3:
        dy = speed
    else:
        dy = -speed
    board[x][y] = shark_id
    shark[shark_id] = (x, y, dx, dy, mass)
fisher = 0
ans = 0
while fisher < c:
    fisher += 1
    for i in range(1, r + 1):
        if board[i][fisher] != 0:
            ans += shark[board[i][fisher]][-1]
            del shark[board[i][fisher]]
            board[i][fisher] = 0
            break
    for id_now, value in shark.items():
        xn, yn, dxn, dyn, mn = value
        if 1 <= xn + dxn <= r and 1 <= yn + dyn <= c:
            nx = xn + dxn
            ny = yn + dyn
        elif xn + dxn < 1 or xn + dxn > r:
            for _ in range(abs(dxn)):
                if dxn < 0:
                    if xn == 1:
                        xn = 2
                        dxn *= -1
                    else:
                        xn -= 1
                else:
                    if xn == r:
                        xn = r - 1
                        dxn *= -1
                    else:
                        xn += 1
            nx, ny = xn, yn
        else:
            for _ in range(abs(dyn)):
                if dyn < 0:
                    if yn == 1:
                        yn = 2
                        dyn *= -1
                    else:
                        yn -= 1
                else:
                    if yn == c:
                        yn = c - 1
                        dyn *= -1
                    else:
                        yn += 1
            nx, ny = xn, yn
        shark[id_now] = (nx, ny, dxn, dyn, mn)
    board = [[0] * (c + 1) for _ in range(r + 1)]
    dead = []
    for shark_id, value in shark.items():
        x, y, dx, dy, m = value
        will_go = board[x][y]
        if will_go == 0:
            board[x][y] = shark_id
        else:
            if shark[will_go][-1] > m:
                dead.append(shark_id)
            else:
                dead.append(will_go)
                board[x][y] = shark_id
    for bye in dead:
        del shark[bye]
print(ans)
