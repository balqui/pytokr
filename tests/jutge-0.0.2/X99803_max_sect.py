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

a, b = int(item()), int(item())
c = "no"
m = None

for v in items():
    v = int(v)
    if c == "yes" and v == b:
        c = "done"
        break
    elif c == "yes" and (m is None or v > m):
        m = v
    elif c == "no" and v == a:
        c = "yes"

if c == "done" and m is None:
    print("empty section")
elif c == "done":
    print(f"maximum is: {m}")
else:
    print("nonexistent section")
