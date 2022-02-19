from sys import stdin as s


def matrix_multiple(first, second=None):
    if not second:
        second = first
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += first[i][k] * second[k][j]
            result[i][j] %= 1000000007
    return result


n = int(s.readline())
if n == 0:
    print(0)
else:
    x = [[0, 1], [1, 1]]
    ans = [[1, 0], [0, 1]]
    n -= 1
    while n > 0:
        if n & 1:
            ans = matrix_multiple(ans, x)
        x = matrix_multiple(x)
        n >>= 1
    print(ans[1][1])
