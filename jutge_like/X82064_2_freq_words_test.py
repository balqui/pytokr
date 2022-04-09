
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

lim = int(item())

from collections import defaultdict as dd

frq = dd(int)
m = set()

for w in items():
    frq[w] += 1
    if frq[w] >= lim: # and len(m) < 2: # difference between accepted and TLE :(
        m.add(w)
if len(m) < 2:
    print(f'Less than two words appear {lim} or more times.')
else:
    print(f'There are two words that appear {lim} or more times.')
