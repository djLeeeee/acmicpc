# 1450 냅색문제
# 반으로 나누고, 왼쪽 꺼 합 구하고 오른쪽 꺼 합 구하기
# 오른쪽 합 정렬해주고 왼쪽 꺼 하나씩 훑으면서 가능한 조합 갯수 찾기
# 오른쪽 합 부분은 이진 탐색 진행해주면 될 듯.
# 왼쪽 합에서 k를 뽑았다면 c + 1 - k 의 idx 찾아주면 되지 않을까?
# 이진 탐색 idx 와의 사투가 아주 차암 재밌었다
from sys import stdin as s

input = s.readline


def search(array, target):
    start = 0
    end = len(array)
    while start < end:
        middle = (start + end) // 2
        if array[middle] <= target:
            start = middle + 1
        else:
            end = middle
    return end


n, c = map(int, input().split())
mass = list(map(int, input().split()))
sum_left = []
m = n - n // 2
n //= 2
for i in range(1 << n):
    s = 0
    for j in range(n):
        if i >> j & 1:
            s += mass[j]
    sum_left.append(s)
sum_left.sort()
ans = 0
for p in range(1 << m):
    t = 0
    for q in range(m):
        if p >> q & 1:
            t += mass[n + q]
    ans += search(sum_left, c - t)
print(ans)
