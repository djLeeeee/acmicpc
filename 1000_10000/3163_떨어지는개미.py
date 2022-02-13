# 3163 떨어지는 개미
# 화살표 개수 = 그 방향으로 떨어질 개미 수
# 앞에서부터 갱신하면 해당 개미가 왼쪽으로 언제 떨어질 지 알 수 있는 듯.

from sys import stdin as s
from collections import deque

t = int(s.readline())

for _ in range(t):
    n, stick, nth_fall = map(int, s.readline().split())
    
    # time = [ ]
    # stay = deque()
    # for _ in range(n):
    #     position, id = map(int, s.readline().split())
    #     stay.append([position, id, 0])
    #     if id < 0:
    #         num = len(stay)
    #         t = 0
    #         y = stay.pop()
    #         for _ in range(num - 1):
    #             x = stay.pop()
    #             t += y[0] - x[0]
    #             x[2] += t
    #             y[2] += t
    #             stay.appendleft(y)
    #             y = x
    #         time.append((y[0] + y[2], y[1]))
    # for _ in range(len(stay)):
    #     w = stay.pop()
    #     time.append((stick - w[0] + w[2], w[1]))
    # time.sort()
    # print(time[nth_fall - 1][1])
    # for t in time:
    #     print(*t)

    # 문제를 잘못 접근했다.
    # 하나씩 계산해줄 필요없음.
    # 남아있는 개미들은 막대 끝에 가까운 애 둘 중 하나가 떨어질 거고
    # 떨어지는 순서는 충돌없이 떨어지는 방향이랑 같아야 한다(충돌하는 개미는 자기 원래 위치까지 돌아갈 때 걸리는 시간이 서로 같다)
    
    ideal = []
    real = deque()
    for _ in range(n):
        position, id = map(int, s.readline().split())
        real.append([position, id])
        if id > 0:
            ideal.append([stick - position, 1])
        else:
            ideal.append([position, -1])
    ideal.sort()
    ans = [ ]
    i = 0
    while i < nth_fall:
        if i + 1 < n:
            left = real[0]
            right = real[-1]
            if ideal[i][0] == ideal[i + 1][0]:
                if left[1] < right[1]:
                    ans.append(left[1])
                    real.popleft()
                    ans.append(right[1])
                    real.pop()
                    i += 1
                else:
                    ans.append(right[1])
                    real.pop()
                    ans.append(left[1])
                    real.popleft()
                    i += 1
            else:
                if ideal[i][1] > 0:
                    ans.append(right[1])
                    real.pop()
                else:
                    ans.append(left[1])
                    real.popleft()
        else:
            ans.append(real[0][1])
        i += 1
    print(ans[nth_fall - 1])