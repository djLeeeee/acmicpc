# 1644 소수의 합
# 두포인터 / 에라토스테네스의 체 융합 문제

from sys import stdin as s
from tempfile import TemporaryFile

def prime_list(num):
    eratos = [1] * (num + 1)
    eratos[0], eratos[1] = 0, 0
    result = [ ] 
    for i in range(2, num + 1):
        if eratos[i] == 1:
            result.append(i)
            x = i
            while x <= num:
                eratos[x] = 0
                x += i
    return result

n = int(s.readline())
if n == 1:
    print(0)
else:
    my_list = prime_list(n)
    length = len(my_list)
    start = 0
    end = 0
    s = my_list[0]
    ans = 0
    while start <= end:
        if s > n:
            s -= my_list[start]
            start += 1
        elif s < n:
            try:
                end += 1
                s += my_list[end]
            except:
                break
        else:
            ans += 1
            end += 1
            start += 1
            try:
                s += my_list[end]
                s -= my_list[start - 1]
            except:
                break
    print(ans)