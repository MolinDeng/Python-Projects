def triangles():
	n = 1
	while True:
		if n == 1:
			L = [1]
			n += 1
			yield L
		elif n == 2:
			L = [1, 1]
			n += 1
			yield L
		else:
			L = [L[i]+L[i+1] for i in range(n-2)]
			L.append(1)
			L.insert(0,1)
			n += 1
			yield L
#more simplify
def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i-1]+L[i] for i in range(len(L))]
