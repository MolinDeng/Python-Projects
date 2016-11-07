from functools import reduce
s = input('Please input a string representing a float: ')
def f(x, y):
	return x*10+y
		
def char2num(key):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[key]

def str2float(s1):
	return reduce(f,map(char2num,s1[:s1.find('.')]+s1[s1.find('.')+1:]))/(10**(len(s1)-1-s1.find('.')))

print(str2float(s))