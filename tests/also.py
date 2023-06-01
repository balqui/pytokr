from pytokr import pytokr

item, items = pytokr(iter = True)

l = list()

for it in items():
	l.append(it)
	l.append(item())
	
# ~ l = [ i for i in items() ]
print(l)
