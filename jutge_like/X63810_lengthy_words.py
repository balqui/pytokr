
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

dd = ddd(list)
mlen = 0

for w in items():
    dd[len(w)].append(w)
    if len(dd[len(w)]) > 1 and len(w) > mlen:
        mlen = len(w)
if mlen == 0:
    print("All words have different lengths")
else:
    print(' '.join(dd[mlen]))
