from sys import stdin

input = stdin.readline

n, b, c = map(int, input().split())
ramen = list(map(int, input().split()))
ans = 0
if b > c:
    for i in range(n - 2):
        if ramen[i]:
            if ramen[i + 1] > ramen[i + 2]:
                x = min(ramen[i], ramen[i + 1] - ramen[i + 2])
                ans += (b + c) * x
                ramen[i] -= x
                ramen[i + 1] -= x
                y = min(ramen[i], ramen[i + 2])
                ans += (b + 2 * c) * y
                ramen[i] -= y
                ramen[i + 1] -= y
                ramen[i + 2] -= y
            else:
                z = min(ramen[i:i+3])
                ans += (b + 2 * c) * z
                ramen[i] -= z
                ramen[i + 1] -= z
                ramen[i + 2] -= z
                w = min(ramen[i:i+2])
                ans += (b + c) * w
                ramen[i] -= w
                ramen[i + 1] -= w
            ans += b * ramen[i]
            ramen[i] = 0
    ans += (b + c) * min(ramen[n - 2:]) + b * abs(ramen[-1] - ramen[-2])
    print(ans)
else:
    print(b * sum(ramen))
