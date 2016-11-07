from functools import reduce
L1 = [1,3,5,7,9]
def f(x,y):
	return x*y
def prod(L):
	return reduce(f,L)

print(prod(L1))