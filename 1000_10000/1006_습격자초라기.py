from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(1 if arr[0][0] + arr[1][0] <= m else 2)
        continue
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = 1 if arr[0][0] + arr[1][0] <= m else 2
    dp[0][1], dp[0][2] = 1, 1
    for i in range(1, n):
        u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
        d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
        h = 1 if arr[0][i] + arr[1][i] <= m else 2
        dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
        dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
        dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
    ans = dp[-1][0]
    if arr[0][0] + arr[0][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][1] = 1
        dp[0][0] = 2
        for i in range(1, n):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-1][2])
    if arr[1][0] + arr[1][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][2] = 1
        dp[0][0] = 2
        for i in range(1, n):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-1][1])
    if arr[0][0] + arr[0][-1] <= m and arr[1][0] + arr[1][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 2
        for i in range(1, n - 1):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-2][0])
    print(ans)
