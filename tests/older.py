from pytokr import item

l = list()

while True:
	try:
		l.append(item())
	except StopIteration:
		break

# ~ l = [ i for i in items() ]
print(l)
