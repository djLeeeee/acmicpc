# 1787 문자열의 주기 예측
# NO MORE KMP
# 싹 다 갈아엎고 스택 구조로 풀어보면??

from sys import stdin as s

n = int(s.readline())
string = s.readline().strip()
ans = 0
stack = []
for idx in range(1, n):
    print(stack)
    if not stack and string[idx] == string[0]:
        ans += idx
        stack.append(1)
    elif stack:
        if string[idx] == string[0]:
            stack.append(0)
        possible = []
        for i in range(len(stack)):
            if string[idx] == string[stack[i]]:
                possible.append(idx - stack[i])
                stack[i] += 1
        if possible:
            ans += max(possible)
        else:
            stack = []
    else:
        stack = []
    print(ans)









