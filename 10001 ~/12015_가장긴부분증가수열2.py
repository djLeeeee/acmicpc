# 가장 긴 증가 부분 수열 찾기
# dp는 n^2의 시간 복잡도 -> 시간 초과
# 이분탐색으로 갱신을 하라는데,, 일단 해보자

from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
ans = [array[0]]


def update_array(my_array, num):
    if my_array[-1] < num:
        my_array.append(num)
    elif my_array[-1] > num:
        start = 1
        end = len(my_array)
        result = end
        while start <= end:
            search = (start + end) // 2
            if my_array[search - 1] >= num:
                result = min(result, search)
                end = search - 1
            elif my_array[search - 1] < num:
                start = search + 1
        my_array[result - 1] = num
    return my_array


for i in array:
    ans = update_array(ans, i)
print(len(ans))
