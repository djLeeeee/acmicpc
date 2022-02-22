# 19134 2x + 2
# 이딴게... 플 4?
# 어려운 로직은 아닌데, 연산량을 최소화 시키기 위해 고민해봤다.

n = int(input())
if n <= 3:
    print(n)
else:
    start = 1
    ans = 0
    div = 2
    while start <= n:
        ans += (n - start) // div + 1
        start = start * 4 + 6
        div *= 4
    two = 2
    while two <= n:
        ans += 1
        two = two * 4 + 6
    print(ans)
