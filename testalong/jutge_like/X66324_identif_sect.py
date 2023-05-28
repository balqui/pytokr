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

for a in items():
    a = int(a)
    b, n = int(item()), int(item())
    s = list()
    c = "no"
    for _ in range(n):
        v = int(item())
        if c == "yes" and v == b:
            c = "done"
        elif c == "yes":
            s.append(v)
        elif c == "no" and v == a:
            c = "yes"
    if c == "done":
        for e in s:
            print(e, end = ' ')
    print()
    print('-' * 10)
