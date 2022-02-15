# 1208 부분수열의 합 3트
# 수업 때 배운 비트 이동 덕분에 컷

from sys import stdin as st

n, s = map(int, st.readline().split())
array = list(map(int, st.readline().split()))
left = array[:n // 2]
right = array[n // 2:]
left_sum = {}
for i in range(1 << (n // 2)):
    my_sum = 0
    for j in range(n // 2):
        if 1 << j & i:
            my_sum += left[j]
    left_sum[my_sum] = left_sum.get(my_sum, 0) + 1
ans = 0
m = n - n // 2
for i in range(1 << m):
    my_sum = 0
    for j in range(m):
        if 1 << j & i:
            my_sum += right[j]
    ans += left_sum.get(s - my_sum, 0)
if s == 0:
    ans -= 1
print(ans)
