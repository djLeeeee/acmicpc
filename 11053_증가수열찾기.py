# dp 알고리즘 공부
# 1. 추가로 들어온 수에 대해 수열 뒤에 붙인 거 안 붙인 거 각각 생성
#    최악의 경우 2^N 복잡도
# 2. key = 끝값 value = 수열 길이? n^2 복잡도?
#    main issue : 새로 들어온 숫자보다 작은 숫자로 끝나는 수열 중 가장 긴 거 찾기

from sys import stdin as s

a = int( s.readline() )
num_list = list( map(int, s.readline().split() ) )

# 1번 / 메모리 초과
# dp = [ [ num_list[0] ] ]
# for i in num_list[1:]:
#     n = True
#     for j in dp:
#         if j[-1] < i:
#             j.append(i)
#             n = False
#     if n:
#         dp.append([i])
# x = max( dp, key = lambda n: len(n) )
# print(len(x))

dp = [1 for _ in range(a)]
for i in range(a):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))