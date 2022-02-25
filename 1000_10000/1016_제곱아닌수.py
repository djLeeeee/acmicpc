# max의 루트의 정수값보다 작거나 같은 소수에 대해 진행?
# 시간복잡도 : 루트 계산 1 / 소수 찾기 n / 체로 거르기 n => 될듯?


from sys import stdin as s
from math import ceil

m, M = map(int, s.readline().split())

# 처음에 한 방법 : 소수 list 만들고 소수^2 에 대해 또 다시 에라토스 체 작업
# 시간초과 / 각 p^2에 대해 list comprehension으로 작업한게 주요원인일 듯.
# if M < 4:
#     print(M - m + 1)
# else:
#     sq = int(M ** 0.5)
#     nums = [ i for i in range(2, sq + 1) ]
#     prime = [ ]
#     while nums:
#         prime.append(nums[0])
#         nums = [ j for j in nums if j % nums[0] ]
#     result = [k for k in range(m, M + 1)]
#     for p in prime:
#         result = [ n for n in result if n % (p ** 2)]
#     print(len(result))

# 두번째 방법: M과 m을 나눈 몫을 이용해 답을 계산
# 틀렸음 => 포함배제 적용 필요, 알고리즘이 더 복잡해져서 이 방법은 포기
# 이후 set으로 받아 update하는 식으로 진행했지만, 이것도 시간초과
# update도 시간복잡도가 높은 작업인 듯? 검색에선 잘 안 나옴.

# 세번째 방법 : 첫번째 방법과 비슷
# 구간 길이가 구간에 있는 값들보다 훨씬 작다! => 2108번 통계학 때랑 비슷
# nums를 다른 방법으로 표시 => set(list) 작업 거치지 않아도 update에 용이하다 / 통과
sq = int(M ** 0.5)
nums = [1] * (M - m + 1)
n = 2
while n <= sq:
    x = ceil(m / (n * n))
    while x * n * n <= M:
        nums[x * n * n - m] = 0
        x += 1
    n += 1
print(sum(nums))
