# DP 알고리즘 / LCS
# 공통 부분 문자열 최대 길이 출력

from sys import stdin as s

A =  s.readline().strip()
B =  s.readline().strip()

la = len(A)
lb= len(B)

dp = [ [0] * (lb + 1) for _ in range(la + 1) ]
for y in range(1, lb + 1):
    for x in range(1, la + 1):
        if A[x - 1] == B[y - 1]:
            dp[x][y] = dp[x - 1][y - 1] + 1
        else:
            dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
print(dp[-1][-1])