
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

points = dict()

n = int(item())

for _ in range(n):
    name = item()
    points[int(item())] = name

c = 0
for p in reversed(sorted(points.keys())):
    c += 1
    if c == 1: print("Gold:", end = ' ')
    elif c == 2: print("Silver:", end = ' ')
    elif c == 3: print("Bronze:", end = ' ')
    print(points[p])
