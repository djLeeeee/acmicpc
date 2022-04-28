n = int(input())
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    if num % 2:
        grundy ^= num - 2
    else:
        grundy ^= num - 2
players = ['Whiteking', 'Blackking']
first = input()
for player in players:
    if player != first:
        second = player
print(first if grundy else second)
