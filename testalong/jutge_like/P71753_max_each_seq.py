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


for n in items():
    m = int(item())
    for i in range(int(n)-1):
        p = int(item())
        if p > m:
            m = p
    print(m)
