# 2473 세용액 / 못 푼지 1년째
# 오늘 어떻게든 풀기
# 투포인터로 해결 완료!

from sys import stdin as s

n = int(s.readline())
liquid = list(map(int, s.readline().split()))
liquid.sort()

combination = abs(sum(liquid[:3]))
result = [0, 1, 2]

for i in range(n - 2):
    x = i + 1
    y = n - 1
    while x != y:
        my_sum = liquid[i] + liquid[x] + liquid[y]
        if abs(my_sum) < combination:
            result = [i, x, y]
            combination = abs(my_sum)       
        if my_sum < 0:
            x += 1
        elif my_sum > 0:
            y -= 1
        else:
            print(liquid[i], liquid[x], liquid[y])
            exit(0)

for j in result:
    print(liquid[j], end = ' ')