from functools import reduce
def is_palindrom1(n):
	return str(n) == str(n)[::-1]

def is_palindrom2(n):
	return str(n) == reduce(lambda x,y: y+x, str(n))

output1 = filter(is_palindrom1, range(0,1000))
output2 = filter(is_palindrom2, range(0,1000))

print('output1 is', list(output1))	
print('output2 is', list(output2))