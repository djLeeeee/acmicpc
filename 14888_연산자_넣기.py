def put_operators(x,pl,mi,pr,di):
    global my_result
    if pl == 0 and mi == 0 and pr == 0 and di == 0:
        my_result.append(x)
        return
    else:
        opnums = pl + mi + pr + di
        if pl > 0:
            y = x + my_list[N - opnums]
            
            put_operators(y, pl - 1, mi, pr, di)
        if mi > 0:
            y = x - my_list[N - opnums]
            put_operators(y, pl, mi - 1, pr, di)
        if pr > 0:
            y = x * my_list[N - opnums]
            put_operators(y, pl, mi, pr - 1, di)
        if di > 0:
            if x < 0:
                x = - x
                y = x // my_list[N - opnums]
                y = - y
            else:
                y = x // my_list[N - opnums]
            put_operators(y, pl, mi, pr, di - 1)       


N = int(input())
my_list = list(map(int, input().split()))
my_result = [ ]
a, b, c, d = map(int, input().split())
put_operators(my_list[0], a, b, c, d)
print(max(my_result))
print(min(my_result))