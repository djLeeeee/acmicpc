# 17298 오큰수

from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
ans = [-1] * n
remain = [0]
for i in range(1, n):
    # remain 에 남아있는 놈들은 내림차순일 것임!
    while remain and array[remain[-1]] < array[i]:
        ans[remain.pop()] = array[i]
    remain.append(i)
print(*ans)

