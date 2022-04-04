# ~ from pytokr import get_tok, get_toks

def make_tokr(f = None):
    "make iterator and next functions out of iterable of split strings"

    from itertools import chain

    def sp(ln):
        "to split the strings with a map"
        return ln.split()

    def the_it():
        "so that both, items and item, are called with parentheses"
        return it

    if f is None:
        from sys import stdin as f
    it = chain.from_iterable(map(sp, f))
    return the_it, it.__next__


items, item = make_tokr()

def collatz_next(n):
	'''
	Returns number following n in the Collatz sequence
	>>> collatz_next(5)
	16
	>>> collatz_next(16)
	8
	>>> collatz_next(13)
	40
	'''
	if n % 2 == 1:
		return 3 * n + 1
	else:
		return n//2

for n in items():
	c = 0
	n = int(n)
	while n != 1:
		n = collatz_next(n)
		c += 1
	print(c)
