from sys import stdin

input = stdin.readline

n = int(input())
ramen = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    if ramen[i]:
        if ramen[i + 1] > ramen[i + 2]:
            x = min(ramen[i], ramen[i + 1] - ramen[i + 2])
            ans += 5 * x
            ramen[i] -= x
            ramen[i + 1] -= x
            y = min(ramen[i], ramen[i + 2])
            ans += 7 * y
            ramen[i] -= y
            ramen[i + 1] -= y
            ramen[i + 2] -= y
        else:
            z = min(ramen[i:i+3])
            ans += 7 * z
            ramen[i] -= z
            ramen[i + 1] -= z
            ramen[i + 2] -= z
            w = min(ramen[i:i+2])
            ans += 5 * w
            ramen[i] -= w
            ramen[i + 1] -= w
        ans += 3 * ramen[i]
        ramen[i] = 0
ans += 5 * min(ramen[n - 2:]) + 3 * abs(ramen[-1] - ramen[-2])
print(ans)
