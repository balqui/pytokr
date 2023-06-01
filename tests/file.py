from pytokr import pytokr

with open("also.py") as f:
	item, items = pytokr(f, iter = True)
	
	l = list()
	l.append(item())
	
	for it in items():
		l.append(it)
		l.append(item())
	
# ~ l = [ i for i in items() ]
print(l)
