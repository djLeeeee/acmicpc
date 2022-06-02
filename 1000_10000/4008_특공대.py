from sys import stdin

input = stdin.readline

n = int(input())
a, b, c = map(int, input().split())
cp = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    cp[i] += cp[i - 1]
dp = [0] * (n + 1)
cht = [(-float('inf'), 0)]
for i in range(1, n + 1):
    start = 0
    end = len(cht) - 1
    while start <= end:
        mid = (start + end) // 2
        if cht[mid][0] <= cp[i]:
            res = cht[mid][1]
            start = mid + 1
        else:
            end = mid - 1
    t = cp[i] - cp[res]
    dp[i] = dp[res] + a * t * t + b * t + c
    for res in range(len(cht) - 1, -1, -1):
        s, k = cht[res]
        t = (dp[i] - dp[k] + a * (cp[i] * cp[i] - cp[k] * cp[k]) - b * (cp[i] - cp[k]))
        t /= 2 * a * (cp[i] - cp[k])
        if t > s:
            break
        else:
            cht.pop()
    cht.append((t, i))
print(dp[-1])
