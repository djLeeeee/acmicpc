from sys import stdin

N, M, K = map( int, stdin.readline().split() )

Tree = [0] * 3 * N
my_list=[]
for _ in range(N):
    my_list.append( int( stdin.readline() ) )

# Segment tree 만들기
def make_a_leaf(x, y, index):
    if x == y:
        Tree[index] = my_list[x]
        return my_list[x]
    else:
        a = make_a_leaf( x, ( x + y ) // 2, 2 * index )
        b = make_a_leaf( ( x + y ) // 2 + 1, y, 2 * index +1 )
        return  a + b

# Segment tree sum 값 구하는 함수
def sum_tree(x, y):

    
    pass

# Segment tree update하는 함수
def update_tree(x, y):


    pass

# 답 구하기
total = make_a_leaf ( 0, N-1, 1 )
for _ in range( M + K ):
    case, a, b = map( int, stdin.readline().split() )
    if case == 1:
        update_tree( a, b )
    else:
        sum_tree( a, b )
