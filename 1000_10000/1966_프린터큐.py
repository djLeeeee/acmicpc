from collections import deque
from sys import stdin as s

t = int( s.readline() )
d = deque()

for _ in range(t):
    a, b = map(int, s.readline().split())
    nums = deque( map( int, s.readline().split() ) )
    index = b
    result = 1
    while True:
        if max(nums) == nums [0]:
            if index == 0:
                print(result)
                break
            else:
                x = nums.popleft()
                result += 1
                index -= 1
        else:
            y = nums.popleft()
            nums.append(y)
            if index:
                index -= 1
            else:
                index = len(nums) - 1