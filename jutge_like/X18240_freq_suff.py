
def make_tokr(f=None):
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


from collections import defaultdict as ddd

def sf(w):
	if len(w) > 2:
		return w[-3:]

dd = ddd(set)

for w in items():
	s = sf(w)
	if s:
		dd[s].add(w)
for s in sorted(dd):
	if len(dd[s]) > 1:
		print(s + ":", len(dd[s]), ' '.join(sorted(dd[s])))
