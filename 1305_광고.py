# 1305 광고 플4 도전~
# KMP 알고리즘 문제

from sys import stdin as s

# 시간초과
# def check_fix(word):
#     length = len(word)
#     moved = 1
#     while moved < length:
#         i = 0
#         find = True
#         while i + moved < length:
#             if word[i] == word[i + moved]:
#                 i += 1
#             else:
#                 find = False
#                 break
#         if find:
#             break
#         moved += 1
#     return moved

# 통과 - kmp 알고리즘
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
word = s.readline().strip()
print(check_fix(word))