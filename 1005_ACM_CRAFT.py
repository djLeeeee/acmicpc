# 1005 ACM Craft
# 위상정렬 ㄲㄲ 연습되도록 새로 짜보기
# 역방향 진행이 훨씬 나을 듯
# 최대 시간 어떻게 뽑아낼지 생각 필요
# 경로 상 최대 시간이 항상 정답인가? -> ㅇㅇ
# 정방향 진행하고 dp로 가면서 승리 조건 달성 시 break?
# dummy 건물 지을수도 있으므로 무조건 역방향이 유리함.
# 시작 노드는 승리 조건 노드로 설정하면 됨


###########################################################
# 역방향 진행 / 시간초과 /  왜 시간초과인지 이해가 전혀 안 됨 
# from sys import stdin as s
# from collections import deque

# T = int(s.readline())

# for _ in range(T):
#     n, k  = map(int, s.readline().split())
#     time = [0] + list(map(int, s.readline().split()))
#     connection = [[] for _ in range(n + 1)]
#     dp = [0] * (n + 1)
#     for _ in range(k):
#         x, y = map(int, s.readline().split())
#         connection[y].append(x)
#     win = int(s.readline())
#     leave = deque([win])
#     dp[win] = time[win]
#     while leave:
#         a = leave.popleft()
#         for i in connection[a]:
#             leave.append(i)
#             dp[i] = max(dp[i], dp[a] + time[i])
#     print(max(dp))

###########################################################
# 정방향
# 오히려 이게 통과함
# 이해 불가ㅏㅏㅏ
from sys import stdin as s
from collections import deque

T = int(s.readline())

for _ in range(T):
    n, k  = map(int, s.readline().split())
    time = [0] + list(map(int, s.readline().split()))
    connection = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    get_in = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, s.readline().split())
        connection[x].append(y)
        get_in[y] += 1
    leaves = deque()
    for i in range(1, n + 1):
        if get_in[i] == 0:
            leaves.append(i)
            dp[i] = time[i]
    while leaves:
        a = leaves.popleft()
        for j in connection[a]:
            dp[j] = max(dp[j], dp[a] + time[j])
            get_in[j] -= 1
            if get_in[j] == 0:
                leaves.append(j)
    print(dp[int(s.readline())])