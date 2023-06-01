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


def leapyear(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def corrdate(d, m, y):
    return (d in range(1, 31) and m in (4, 6, 9, 11) or
            d in range(1, 32) and m in (1, 3, 5, 7, 8, 10, 12) or
            d in range(1, 29) and m == 2 or
            d == 29 and m == 2 and leapyear(y))


for d in items():
    m, y = item(), item()
    if corrdate(int(d), int(m), int(y)):
        print("Correct Date")
    else:
	    print("Incorrect Date")
