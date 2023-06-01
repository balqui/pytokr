from pytokr import make_tokr

items, item = make_tokr()

print(item())
print(item())
print(item())
l = [ i for i in items() ]
print(l)
