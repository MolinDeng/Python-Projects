L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower()
print(sorted(L,key = by_name))

def by_score(t):
	return t[1]
print(sorted(L,key = by_score))