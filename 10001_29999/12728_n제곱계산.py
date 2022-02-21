# 12728 n 제곱 계산
# 점화식 세우기 문제.

from sys import stdin as s

input = s.readline

n = int(input())


def multiple(first, second=None):
    if not second:
        second = first
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            ans[i][j] += first[i][0] * second[0][j]
            ans[i][j] += first[i][1] * second[1][j]
    return ans


for t in range(1, n + 1):
    k = int(input())
    k -= 1
    # 3자리 수만 보는 거니까, 1000으로 나눠주자
    k %= 1000
    x = [[1, 0], [0, 1]]
    # 3 + sqrt(5) 가 만족하는 이차 방정식에 대해서 생각해보자
    # 3 - sqrt(5) 는 0과 1 사이니 아무리 곱해도 0과 1 사이다
    # 근데 둘의 합을 구하는 점화식은 쉽게 구할 수 있다!
    matrix = [[6, -4], [1, 0]]
    while k > 0:
        if k & 1:
            x = multiple(x, matrix)
        k >>= 1
        matrix = multiple(matrix)
    print(f'Case #{t}: ', end='')
    answer = int(x[0][0] * 6 + x[0][1] * 2) % 1000 - 1
    if answer == -1:
        answer = 999
    answer = str(answer)
    while len(answer) < 3:
        answer = '0' + answer
    print(answer)
