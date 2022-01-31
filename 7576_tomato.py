# 7576 토마토
# 처음엔 재귀로 풀었는데 시간 초과 뜸 / 배추 벌레 코드에서 조금 바꾼 형태
# 그래서 while 문으로 BFS 탐색을 진행. 시간은 좀 걸렸지만 통과

from sys import stdin as s

# 메모리 초과 / 재귀로 푼 경우
# import sys
# sys.setrecursionlimit(10 ** 6)

# def tomato(a, b, n):
# 	if 0 <= a < x and 0 <= b < y:
# 		if g[b][a] > n or g[b][a] == 0 or n == 1:
# 			g[b][a] = n
# 			tomato(a - 1, b, n + 1)
# 			tomato(a, b - 1, n + 1)
# 			tomato(a + 1, b, n + 1)
# 			tomato(a, b + 1, n + 1)


# x, y = map(int, sys.stdin.readline().split())
# g = [ ]
# start = [ ]
# for i in range(y):
# 	a = list(map(int, sys.stdin.readline().split()))
# 	for j in range(x):
# 		if a[j] == 1:
# 			start.append([j, i])
# 	g.append(a)

# for k in start:
# 	tomato(k[0], k[1], 1)
# result = [ ]
# for p in g:
# 	result += p
# if result.count(0):
# 	print(-1)
# else:
# 	print(max(result) - 1)


# 통과 / while문으로 풀음
def tomato(start_points, M, N, g):
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	result = 0
	while start_points:
		result += 1
		new = [ ]
		for i in range(len(start_points)):
			x, y = start_points[i]
			for j in range(4):
				p = x + dx[j]
				q = y + dy[j]
				if 0 <= p < N and 0 <= q < M and g[p][q] == 0:
					new.append([p, q])
					g[p][q] = result
		start_points = new
	for k in g:
		if 0 in k:
			return -1
	return result - 1


M, N = map(int, s.readline().split())
g = [ ]
start_points = [ ]
for i in range(N):
	a = list(map(int, s.readline().split()))
	for j in range(M):
		if a[j] == 1:
			start_points.append([i, j])
	g.append(a)
print(tomato(start_points, M, N, g))