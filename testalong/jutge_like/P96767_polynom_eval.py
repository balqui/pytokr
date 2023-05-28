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


x = float(item())
x_pow = 1
r = 0

for coef in items():
    r += x_pow * float(coef)
    x_pow *= x

print('{:.4f}'.format(r))
