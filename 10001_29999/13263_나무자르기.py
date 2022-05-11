from sys import stdin

input = stdin.readline

n = int(input())
h = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [0] * n
CHT = [(0, 0)]
for i in range(1, n):
    start = 0
    end = len(CHT) - 1
    while start <= end:
        mid = (start + end) // 2
        if CHT[mid][0] <= h[i]:
            res = CHT[mid][1]
            start = mid + 1
        else:
            end = mid - 1
    dp[i] = dp[res] + c[res] * h[i]
    if i < n - 1:
        while CHT[-1][0] >= (dp[i] - dp[CHT[-1][1]]) / (c[CHT[-1][1]] - c[i]):
            CHT.pop()
        CHT.append(((dp[i] - dp[CHT[-1][1]]) / (c[CHT[-1][1]] - c[i]), i))
print(dp[-1])
