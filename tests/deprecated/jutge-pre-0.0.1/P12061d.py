'''
Based on submission S016, use pytokr; identical to c except import
'''


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

for s in get_toks():
	if s == "beginning" or s == "end":
		break
else:
	s = None

if s != "beginning":
    print("wrong sequence")

else:
    n = 0
    wrong = True
    for s in get_toks():
        if s == "end":
            print(n)
            wrong = False
            break # only change from TLE
        n = n + 1
    if wrong:
        print("wrong sequence")
