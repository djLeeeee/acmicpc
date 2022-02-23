# 2580 스도쿠
# 구현은 둘째치고 시간초과 이슈가 너무 심한 문제
# 재귀로 구현 / 시간 더 줄일 방법 있나?

from sys import stdin as s


def box(x, y, board):  # 해당 위치가 포함된 박스를 반환
    result = []
    for i in range(3):
        result += board[(x // 3) * 3 + i][(y // 3) * 3: (y // 3) * 3 + 3]
    return result


def check_sudoku(x, y, board, p):  # 해당 위치에 p를 넣을 수 있나 체크
    for j in range(9):
        if board[j][y] == p or board[x][j] == p:
            return False
    if p in box(x, y, board):
        return False
    return True


def put_in(n=0):
    if n == len(empty):             # 다 채웠다면 (빈 칸의 수만큼 채웠다면)
        for i in range(9):          # 출력양식에 맞게 출력하고
            print(*sudoku[i])
        exit(0)                     # 그대로 종료
    x = empty[n][0]                 # 아직 덜 채웠으면 빈 칸 좌표 받고
    y = empty[n][1]
    for j in range(1, 10):          # 그 칸에 1부터 9까지 들어갈 수 있는지 체크
        if check_sudoku(x, y, sudoku, j):
            sudoku[x][y] = j        # 해당 칸에 넣을 수 있는 수 넣고
            put_in(n + 1)           # 다음 칸을 넣으러 가자
            sudoku[x][y] = 0        # 코드 종료가 안 됐다면 답이 아니므로 초기화


sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, s.readline().split())))
empty = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            empty.append([r, c])
put_in()
