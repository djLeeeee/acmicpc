from sys import stdin

input = stdin.readline

n = int(input())
goods = [tuple(map(int, input().split())) for _ in range(n)]
goods.sort()
real = [0, goods.pop()]
while goods:
    now = goods.pop()
    if real:
        if real[-1][0] > now[0] and real[-1][1] < now[1]:
            real.append(now)
        elif real[-1][1] < now[1]:
            real.pop()
            real.append(now)
l = len(real)
dp = [0] * l
# (컨벡스 헐 시작점, i with 기울기=h_(i + 1), y절편=dp[i])
# real[j] = hj, wj
CHT = [(0, 0)]
for i in range(1, l):
    start = 0
    end = len(CHT) - 1
    while start <= end:
        middle = (start + end) // 2
        # 볼록 껍질 직선의 시작점이 wi 보다 작다면
        if CHT[middle][0] <= real[i][1]:
            res = CHT[middle][1]
            start = middle + 1
        else:
            end = middle - 1
    dp[i] = real[res + 1][0] * real[i][1] + dp[res]
    if i < l - 1:
        start = 0
        end = len(CHT) - 1
        a2, b2 = real[i + 1][0], dp[i]
        while start <= end:
            middle = (start + end) // 2
            now = CHT[middle][1]
            a1, b1 = real[now + 1][0], dp[now]
            # 시작점 뒤 쪽에 교점이 나온 경우
            s = (b2 - b1) / (a1 - a2)
            if s > CHT[middle][0]:
                res = middle
                ns = s
                start = middle + 1
            else:
                end = middle - 1
        CHT = CHT[:res + 1] + [(ns, i)]
print(dp[-1])
