n = int(input())
start = 1
end = 2 * 10 ** 9
sq = int(end ** 0.5)
check = [1] * (sq + 1)
pr = [4]
for i in range(3, sq + 1, 2):
    if check[i]:
        pr.append(i * i)
        for j in range(i * i, sq + 1, 2 * i):
            check[j] = 0
l = len(pr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = mid
    for p1 in range(l):
        q1 = pr[p1]
        if q1 > mid:
            break
        cnt -= mid // q1
        for p2 in range(p1 + 1, l):
            q2 = q1 * pr[p2]
            if q2 > mid:
                break
            cnt += mid // q2
            for p3 in range(p2 + 1, l):
                q3 = q2 * pr[p3]
                if q3 > mid:
                    break
                cnt -= mid // q3
                for p4 in range(p3 + 1, l):
                    q4 = q3 * pr[p4]
                    if q4 > mid:
                        break
                    cnt += mid // q4
                    for p5 in range(p4 + 1, l):
                        q5 = q4 * pr[p5]
                        if q5 > mid:
                            break
                        cnt -= mid // q5
                        for p6 in range(p5 + 1, l):
                            q6 = q5 * pr[p6]
                            if q6 > mid:
                                break
                            cnt += mid // q6
    if cnt > n:
        end = mid - 1
    elif cnt < n:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)
