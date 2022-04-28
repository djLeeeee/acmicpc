n = int(input())
grundy = [0] * (n + 1)
grundy[2] = 1
for num in range(3, n + 1):
    sub_grundy = set()
    remain = num - 2
    for left in range(remain // 2 + 1):
        right = remain - left
        sub_grundy.add(grundy[left] ^ grundy[right])
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
print('1' if grundy[-1] else '2')
