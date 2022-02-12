# 9935번 / 시간 초과
# main issue : bottleneck이 split? join? in?
# 예상대로 in이 시간초과 원이
# in 안 쓰고 어떻게 진행?
# stack으로 문자열 하나씩 받으면서 진행?

from sys import stdin as s

a = s.readline().rstrip()
b = s.readline().rstrip()

# while True:
#     x = ''.join(a.split(b))
#     if x == a:
#         break
#     else:
#         a = x[:]
# if a:
#     print(a)
# else:
#     print('FRULA')

bomb_l = len(b)
bombtail = b[-1]
stack = [ ]
for i in a:
    stack.append(i)
    if bombtail == i:
        if ''.join(stack[- bomb_l : ]) == b:
            for _ in range(bomb_l):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')