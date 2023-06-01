from pytokr import pytokr

item = pytokr()

l = list()

while True:
	try:
		l.append(item())
	except StopIteration:
		break

# ~ l = [ i for i in items() ]
print(l)
