from sys import stdin

input = stdin.readline

mod = (".00", ".25", ".50", ".75")
for _ in range(int(input())):
    n = int(input())
    statue = [(-10 ** 8, 0)]
    for _ in range(n):
        x, h = map(int, input().split())
        while statue:
            if statue[-1][0] >= x - h:
                statue.pop()
            else:
                break
        if statue[-1][1] < x + h:
            statue.append((x - h, x + h))
    l = len(statue)
    dp = [0] * l
    CHT = [(-float('inf'), 0)]
    for i in range(1, l):
        start = 0
        end = len(CHT) - 1
        while start <= end:
            mid = (start + end) // 2
            if CHT[mid][0] <= statue[i][1]:
                res = CHT[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        dp[i] = dp[res] + (statue[i][1] - statue[res + 1][0]) ** 2
        if i < l - 1:
            for j in range(len(CHT) - 1, -1, -1):
                s, k = CHT[j]
                x = dp[i] - dp[k] + statue[i + 1][0] ** 2 - statue[k + 1][0] ** 2
                x /= 2 * (statue[i + 1][0] - statue[k + 1][0])
                if x < s:
                    CHT.pop()
                else:
                    break
            CHT.append((x, i))
    print(str(dp[-1] // 4) + mod[dp[-1] % 4])
