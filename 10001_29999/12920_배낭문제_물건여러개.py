# 12920 평범한 배낭 / 오늘 마지막
# 물건 개수가 1이 아닌 배낭 문제 -> 일단 배낭 문제랑 똑같이 진행해도 될 거 같긴 함
# 메모리 초과 / 시간 초과 뜸 -> k가 너무 크면 연산량 증가
# 비트마스크 개념 처음 사용 -> n < 2^k에 대해서 1,2,4,...,2^(k-1)의 합으로 표현할 수 있다는 것이 포인트

from sys import stdin as s

m, n = map(int, s.readline().split())

goods = []
dp = [0] * (n + 1)
for _ in range(m):
    v, c, k = map(int, s.readline().split())
    btmsk = 1
    while k > 0:  # 요기 while 문이 비트마스크
        a = min(btmsk, k)
        new_dp = [0] * (n + 1)
        new_dp[:a * v] = dp[:a * v]
        for j in range(a * v, n + 1):
            new_dp[j] = max(dp[j], dp[j - a * v] + a * c)
        dp = new_dp
        k -= btmsk
        btmsk *= 2
print(dp[-1])
