#this algrithm is so beautiful
def _ood_iter():
	n = 1
	while True:
		n += 2
		yield n
def _not_divisible(n):
	return lambda x: x % n > 0
def prime():
	yield 2
	it = _ood_iter()#initialize generator
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)#update the iterator, actually, _not_divisible(n) is 
										  #just like a function, but it's a lambda expression, it
										  #can take the x from sequence <it> as it's parament.
for n in prime():
	if n < 1000:
		print(n)
	else:
		break
