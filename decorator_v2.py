#write a log which can surpport no passing parament and passing parament

import functools
def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log('execute')
def now1():
	print('2016-11-08')
	
@log
def now2():
	print('2016-11-08')
	
now1()
now2()