# 2580 스도쿠
# 구현은 둘째치고 시간초과 이슈가 너무 심한 문제
# 재귀로 구현 / 시간 더 줄일 방법 있나?

from sys import stdin as s

def box(x, y, board):
	result = [ ]
	for i in range(3):
		result += board[(x // 3) * 3 + i][(y // 3) * 3: (y // 3) * 3 + 3]
	return result

def check_sudoku(x, y, board, p):
	cnt_in = [ ]
	for j in range(9):
		if board[j][y] == p or board[x][j] == p:
			return False
	if p in box(x, y, board):
		return False
	return True

def put_in(n = 0):
	if n == len(empty):
		for i in range(9):
			print(*sudoku[i])
		exit(0)
	x = empty[n][0]
	y = empty[n][1]
	for j in range(1, 10):
		if check_sudoku(x, y, sudoku, j):
			sudoku[x][y] = j
			put_in(n + 1)
			sudoku[x][y] = 0

sudoku = [ ]
for _ in range(9):
	sudoku.append(list(map(int, s.readline().split())))
empty = [ ]
for i in range(9):
	for j in range(9):
		if sudoku[i][j] == 0:
			empty.append([i, j])
put_in()