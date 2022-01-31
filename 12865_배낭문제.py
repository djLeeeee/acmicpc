# 12865 배낭문제 / 2차원 dp 알고리즘 
# 로직 확인하자. 하고도 긴가민가하다

from sys import stdin as s

# 시간 초과 코드
# def backpacking(N, M, mass, value):
#     if N <= 0 or M < 0:
#         return 0
#     if mass[N] > M:
#         return backpacking(N - 1, M, mass, value)
#     x = backpacking(N - 1, M - mass[N], mass, value) + value[N]
#     y = backpacking(N - 1, M, mass, value)
#     return max(x, y)

# N, M = map(int, s.readline().split())
# mass = [ 0 ]
# value = [ 0 ]
# for _ in range(N):
#     m, v = map(int, s.readline().split())
#     mass.append(m)
#     value.append(v)
# print(backpacking(N, M, mass, value))


N, M = map(int, s.readline().split())
mv = [0]
for _ in range(N):
	mv.append(list(map(int, s.readline().split())))
dp = [[0] * (M + 1) for _ in range(N + 1)] #dp[i][j] 는 i번째 물품까지 체크했을 때 최대 무게 j로 할 수 있는 최대 가치를 의미
for i in range(1, N + 1):
	for j in range(1, M + 1):
		if mv[i][0] > j: # i번째 물품이 무게 한도 j보다 무거운 상황
			dp[i][j] = dp[i - 1][j]
		else: # 평소의 dp, max(dp[i - 1][j], ... 부분 헷갈리지 말자.
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - mv[i][0]] + mv[i][1]) 
print(dp[i][j])