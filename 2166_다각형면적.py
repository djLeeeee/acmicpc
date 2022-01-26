from sys import stdin as s

# 벡터 외적으로 풀면 될 듯? +- 값 유의 /  최종 값에만 절댓값 씌워주면 될 듯?
# 다행히 둘레 순서대로 점이 주어짐 / 아닐 경우엔 이 방법으론 못 품.

def area(p1, p2, p3):
    v1 = [ p1[0] - p2[0], p1[1] - p2[1] ]
    v2 = [ p1[0] - p3[0], p1[1] - p3[1] ]
    return v1[0] * v2[1] - v1[1] * v2[0]

N = int(s.readline())
points = [ ]
for _ in range(N):
    x, y = map(int, s.readline().split())
    points.append([x, y])
result = 0
for i in range(2, N):
    result += area(points[0], points[i - 1], points[i]) # 직접 그려보면 points[0] 들어가야 하는 거 알 수 있음
result = abs(result) / 2
print('{0:.1f}'.format(result))