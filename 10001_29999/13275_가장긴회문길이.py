from sys import stdin as s


# def max_palindrome(my_lst):
#     length = 1
#     p = 1
#     if len(my_lst) == 1:
#         return 1
#     if my_lst[0] == my_lst[1]:
#         length += 1
#         p = 2
#     m = length
#     n = p
#     previous = my_lst[1]
#     for i in range(2, len(my_lst)):
#         if i > length:
#             if length == 1:
#                 if my_lst[i] == my_lst[i - 1]:
#                     length += 1
#                 elif my_lst[i] == my_lst[i - 2]:
#                     length += 2
#             else:
#                 if my_lst[i - length - 1] == my_lst[i]:
#                     length += 2
#                 else:
#                     length = 1
#         else:
#             length = 1
#         m = max(m, length)
#         if previous == my_lst[i]:
#             p += 1
#         else:
#             n = max(n, p)
#             p = 1
#             previous = my_lst
#     return max(m, n, p)
#
#
# while True:
#     print(max_palindrome(input()))

def max_palindrome(my_lst):
    length = 0
    for i in range(len(my_lst)):
        if my_lst[i - length: i + 1] == my_lst[i - length: i + 1][::-1]:
            length += 1
        elif i > length:
            if my_lst[i - length - 1: i + 1] == my_lst[i - length - 1: i + 1][::-1]:
                length += 2
    return length


print(max_palindrome(input()))
