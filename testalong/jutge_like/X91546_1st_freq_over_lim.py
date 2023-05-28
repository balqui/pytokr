# ~ from pytokr import get_tok, get_toks

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
m = None

for w in items():
    frq[w] += 1
    if frq[w] > lim and m is None:
        m = w
if m is None:
    print(f'No words reach above frequency {lim}.')
else:
    print(f'The first word to reach above frequency {lim} is "{m}".')
