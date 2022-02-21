# 13976 타일 채우기
# 비트 연산을 이용한 행렬 거듭 제곱
# 점화식 세우기가 관건!

from sys import stdin as s

input = s.readline

n = int(input())


def matrix_multiple(first, second=None):
    if not second:
        second = first
    size = len(first)
    ans = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += first[i][k] * second[k][j]
            ans[i][j] %= 1000000007
    return ans


if n % 2:
    print(0)
else:
    n //= 2
    n -= 1
    matrix = [[4, -1], [1, 0]]
    x = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            x = matrix_multiple(matrix, x)
        n >>= 1
        matrix = matrix_multiple(matrix)
    print((3 * x[0][0] + x[0][1]) % 1000000007)
