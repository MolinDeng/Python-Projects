L1 = ['adam', 'LISA', 'BiaT', 'LUcy']
def nomalize(s):
	return s[0:1].upper()+s[1:].lower()

print(list(map(nomalize,L1)))