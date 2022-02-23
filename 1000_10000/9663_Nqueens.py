# 9663 N queen 
# 백트래킹 사용

def can_go(x, queen):
    # 세로 체크
    if x in queen:
        return False
    l = len(queen)
    # 대각선 체크
    for n, q in enumerate(queen):
        if abs(q - x) == l - n:
            return False
    return True


def n_queens(n, queen):
    global result
    for i in range(n):
        if can_go(i, queen):                # i 번째에 퀸 배치 가능한가?
            if len(queen) == n - 1:         # 그 퀸이 마지막 퀸인가?
                result += 1                 # 그렇다면 결과 + 1
            else:
                n_queens(n, queen + [i])    # 아직 안 끝났다면 더 진행해라.


result = 0
n_queens(15, [])
print(result)
