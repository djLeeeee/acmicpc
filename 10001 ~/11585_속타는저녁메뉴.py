# 11585 속타는 저녁 메뉴
# KMP 알고리즘 문제

from sys import stdin as s

def check_fix(word):
    l = len(word)
    result = [0] * l
    i = 0
    for j in range(1, l):
        while word[i] != word[j] and i > 0:
            i = result[i - 1] 
        if word[i] == word[j]:
            i += 1
            result[j] = i
    return l - result[-1]

n = int(s.readline())
word = s.readline().strip().replace(' ', '')
s.readline()
x = check_fix(word)
if x == n - 1:
    print('1/1')
elif n % x == 0:
    print(f'1/{x}')
else:
    print(f'1/{n}')