
def f():
	def g():
		print('t' in locals(), "locals g") # always False
		print('t' in globals(), "globals g") # always False
	def h():
		nonlocal t
		print('t' in locals(), "locals h") # first False, then True
		print('t' in globals(), "globals h") # always False
	g()
	h()
	print('t' in locals(), "locals f") # False
	t = 1
	print('t' in locals(), "locals f")  # True
	g()
	h()

# f()

def r(n):
	"change the exception of iterator n"
	MyError = Exception("My error...")
	ok = True
	def m():
		try:
			return n()
		except StopIteration:
			ok = False
		if not ok:
			raise MyError
	return m


t = iter(range(5))

g = r(t.__next__)
print(g())
print(g())
print(t.__next__())
print(t.__next__())
print(g())
print(g())
print(t.__next__())
print(t.__next__())
