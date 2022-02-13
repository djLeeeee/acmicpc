# 2110 공유기 설치
# 이분 탐색???
# 항상 최소 최대 위치에는 하나 설치해야 하는 듯
# -> 최소 위치에 하나 설치하고, 그 이후에 거리 별로 이분 탐색
# 탐색 위치를 이분 탐색해서 하는 것이 아니라,
# 두 집 간의 거리를 이분 탐색 진행하는 것임!


from sys import stdin as s

n, c = map(int, s.readline().split())
wifi = [0] * n
for i in range(n):
    wifi[i] = int(s.readline())
wifi.sort()  # n log n
min_length = 1  # 두 집 간에 떨어질 수 있는 최소 거리
max_length = wifi[-1] - wifi[0]  # 두 집 간에 떨어질 수 있는 최대 거리
result = 0
while min_length <= max_length:
    searching = (min_length + max_length) // 2
    pointer = 0
    chosen = 1
    for j in range(1, n):
        if searching <= wifi[j] - wifi[pointer]:
            chosen += 1
            pointer = j
    if chosen >= c:  # 등호 필수임. chosen >= c면 그대로 지어도 되는 것이니 result 를 갱신.
        result = max(result, searching)
        min_length = searching + 1
    else:
        max_length = searching - 1
print(result)
