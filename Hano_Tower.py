def HanaT(n, a, b, c):
	# if n == 0:
	# 	return
	if n == 1:
		print('%s-->%s'%(a,c))
	else:
		HanaT(n-1, a, c, b)
		HanaT(1, a, b, c)
		HanaT(n-1, b, a, c)

HanaT(3, 'A', 'B', 'C')