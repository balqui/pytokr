def make_get_toks(f=None):
    "make iterator and next functions out of iterable of split strings"
    from sys import stdin
    from itertools import chain

    def sp(ln):
        "to split the strings with a map"
        return ln.split()

    def the_it():
        "so that both results are callable in similar manner"
        return it

    if f is None:
        f = stdin
    it = chain.from_iterable(map(sp, f))
    return the_it, it.__next__


get_toks, get_tok = make_get_toks()



from collections import defaultdict as dd

n, k = int(get_tok()), int(get_tok())

d = dd(int)

on = True

for m in get_toks():
    m = int(m)
    if m % n == 0:
        d[m] += 1
        if d[m] >= k and on:
            print(m)
            on = False
if on:
    print("none")
