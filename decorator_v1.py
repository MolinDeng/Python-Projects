#before function called, print 'begin call',
#after function called, print 'end call'

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call')
		ret = func(*args, **kw)
		print('end call')
		return ret  
	return wrapper
	
@log
def now():
	print('2016-11-08')

now()