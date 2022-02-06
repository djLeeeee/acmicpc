# 11403 경로찾기
# 플로이드 와샬 알고리즘
# 알고리즘 내용 자체가 재밌다. 쓸 곳 많을 듯

from sys import stdin as s

n = int(s.readline())
connection = [ ]
for _ in range(n):
    connection.append(list(map(int, s.readline().split())))

# i가 가운데 노드 / j,k가 양끝 노드
# i = j 또는 i = k 인 상황 상관 없나? 없다 행렬 [i][i] 값 항상 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if connection[j][i] == 1 and connection[i][k] == 1:
                connection[j][k] = 1
for p in range(n):
    print(*connection[p])
