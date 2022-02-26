# 17401 일하는 세포
# 분할 정복으로 행렬 거듭제곱 계산하는 문제인 듯?

from sys import stdin as s

input = s.readline


def multiple_matrix(first, second=None):
    if not second:
        second = first
    sz = len(first)
    res = [[0] * sz for _ in range(sz)]
    for j in range(sz):
        for i in range(sz):
            for k in range(sz):
                res[i][k] += first[i][j] * second[j][k]
    for i in range(sz):
        for j in range(sz):
            res[i][j] %= p
    return res


p = 1000000007
t, n, d = map(int, input().split())
blood_map = {}
for idx in range(t):
    road = [[0] * n for _ in range(n)]
    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        road[a - 1][b - 1] = c
    blood_map[idx] = road
cycle = d // t
remain = d % t
blood = blood_map[0]
for ii in range(1, t):
    blood = multiple_matrix(blood, blood_map[ii])
result = [[0] * n for _ in range(n)]
for jj in range(n):
    result[jj][jj] = 1
while cycle > 0:
    if cycle & 1:
        result = multiple_matrix(result, blood)
    blood = multiple_matrix(blood)
    cycle >>= 1
for kk in range(remain):
    result = multiple_matrix(result, blood_map[kk])
for line in result:
    print(*line)
