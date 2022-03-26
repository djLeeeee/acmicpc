from sys import stdin

input = stdin.readline


def power(a, b, mod):
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result


def Miller_Rabin(num,check):
    if num == check:
        return 1
    k = num - 1
    while True:
        x = power(check, k, num)
        if x == num - 1:
            return 1
        if k % 2:
            if x == 1:
                return 1
            break
        k //= 2
    return 0


ans = 0
for _ in range(int(input())):
    n = 2 * int(input()) + 1
    ans += Miller_Rabin(n, 2) * Miller_Rabin(n, 7) * Miller_Rabin(n, 61)
print(ans)
