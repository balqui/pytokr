

# ~ from pytokr import get_tok

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


def dig2(k):
	if k < 10:
		return '0' + str(k)
	else:
		return str(k)

h = int(item())
m = int(item())
s = int(item())

s += 1

if s == 60:
	s = 0
	m += 1
if m == 60:
	m = 0
	h += 1
if h == 24:
	h = 0

print(dig2(h) + ":" + dig2(m) + ":" + dig2(s))
