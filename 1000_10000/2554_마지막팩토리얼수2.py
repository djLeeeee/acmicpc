tail = {2: 6, 6: 8, 8: 4, 4: 2}
n = int(input())
if n == 1:
    print(1)
    exit()
ans = 1
while n > 0:
    r, s = n // 5, n % 5
    if r % 2:
        ans *= 4
    else:
        ans *= 6
    for ss in range(1, n % 5 + 1):
        ans *= ss
    ans %= 10
    for _ in range(r % 4):
        ans = tail[ans]
    n = r
print(ans)
