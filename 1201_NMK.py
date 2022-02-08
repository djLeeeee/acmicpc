# 1201 NMK
# 덕분에 5천등 이내로 진입!

from sys import stdin as s

n, m, k = map(int, s.readline().split())

if n + 1 < m + k or n > m * k: # 비둘기집 원리
    print(-1)
else:
    # 부분 증가 수열 m 부분 감소수열 k
    # n - m + 2 ~ n 맨 앞에 놓고 (길이 m-1)
    # 최대 길이 k 뒤에 붙이고 번갈아가면서 배치?
    # 감소수열을 앞에 붙이는게 더 편함 -> 1이 제일 작으니까 뒤에 증가수열에 영향 안 끼침
    # 증가수열 앞에 붙이면 뒤 감소수열 길이에 영향을 줌
    # ?? 지금 보니까 둘 다 영향 끼침 상관 없음. 일단 감소 먼저 하는 쪽으로 진행
    # k ~ 1 맨 앞에 놓고 남은 건 k+1 ~ n
    # 
    
    ans = list(range(k, 0, -1))
    # n - k 개 더 쓸 수 있고, 뒤에 감소 수열을 역순으로 m - 1개 붙여주면 됨
    if m != 1:
        length = (n - k) // (m - 1)
        remain = (n - k) % (m - 1)
        for i in range(m - 1 - remain):
            ans.extend(list(range(k + length, k, -1)))
            k += length
        length += 1
        for j in range(remain):
            ans.extend(list(range(k + length, k, -1)))
            k += length
    print(*ans)