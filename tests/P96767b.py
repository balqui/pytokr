

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

x = float(get_tok())
x_pow = 1
r = 0

for coef in get_toks():
    r += x_pow * float(coef)
    x_pow *= x

print('{:.4f}'.format(r))
