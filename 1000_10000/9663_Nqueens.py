# 9663 N queen 
# 백트래킹 사용

def can_go(x, queen):
	if x in queen:
		return False
	l = len(queen)
	for n, q in enumerate(queen):
		if abs(q - x) == l - n:
			return False
	return True

def n_queens(n, queen):
	global result
	# if len(queen) == n:
	# 	result += 1
	# else:
	# 	for i in range(n):
	# 		if can_go(i, queen):
	# 			n_queens(n, queen + [i])
	for i in range(n):
		if can_go(i, queen):
			if len(queen) == n - 1:
				result += 1
			else:
				n_queens(n, queen + [i])

result = 0
n_queens(15, [])
print(result)