from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
input = stdin.readline


def sol(x, y):
    if dp[x][y]:
        return sol(dp[x][y][0] - 1, dp[x][y][1])
    while board[x + 1][y] == '.':
        x += 1
    if board[x + 1][y] == 'X':
        board[x][y] = 'O'
        return x, y
    else:
        if board[x][y - 1] == board[x + 1][y - 1] == '.':
            dp[x + 1][y - 1] = sol(x + 1, y - 1)
            return dp[x + 1][y - 1]
        elif board[x][y + 1] == board[x + 1][y + 1] == '.':
            dp[x + 1][y + 1] = sol(x + 1, y + 1)
            return dp[x + 1][y + 1]
        else:
            board[x][y] = 'O'
            return x, y


n, m = map(int, input().split())
board = [['X'] + list(input().rstrip()) + ['X'] for _ in range(n)]
board.append(['X'] * (m + 2))
dp = [[0] * (m + 2) for _ in range(n)]
for _ in range(int(input())):
    _, _ = sol(-1, int(input()))
for line in board[:-1]:
    print(''.join(line[1:-1]))
