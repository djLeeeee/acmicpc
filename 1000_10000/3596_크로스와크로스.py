n = int(input())
grundy = [0] * (n + 3)
grundy[1] = 1
grundy[2] = 1
grundy[3] = 1
grundy[4] = 2
grundy[5] = 2
for num in range(6, n + 3):
    sub_grundy = set()
    for ex in range(3, 6):
        sub_grundy.add(grundy[num - ex])
    for left in range(1, (num - 5) // 2 + 1):
        right = num - 5 - left
        sub_grundy.add(grundy[left] ^ grundy[right])
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
print('1' if grundy[n] else '2')
