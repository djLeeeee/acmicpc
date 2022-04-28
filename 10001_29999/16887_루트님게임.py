n = int(input())
grundy = 0
for num in map(int, input().split()):
    if 0 <= num < 4 or 82 <= num < 82 * 82:
        pass
    elif 4 <= num < 16 or 15 ** 4 + 1 <= num < (15 ** 4 + 1) ** 2:
        grundy ^= 1
    elif 16 <= num < 81 or 81 ** 4 + 1 <= num:
        grundy ^= 2
    elif 82 ** 2 <= num < 15 ** 4 + 1:
        grundy ^= 3
    else:
        grundy ^= 4
print('koosaga' if grundy else 'cubelover')
