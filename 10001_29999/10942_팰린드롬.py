from sys import stdin as s

input = s.readline

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i + 1][i + 1] = 1
    if array[i] == array[i + 1]:
        dp[i][i + 1] = 1
for length in range(2, n):
    for start in range(1, n - length + 1):
        if dp[start + 1][start + length - 1] and array[start] == array[start + length]:
            dp[start][start + length] = 1
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(dp[x][y])
