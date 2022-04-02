

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

for n in get_toks():
    m = int(get_tok())
    for i in range(int(n)-1):
        p = int(get_tok())
        if p > m:
            m = p
    print(m)
