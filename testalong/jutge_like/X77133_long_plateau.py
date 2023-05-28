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

n = int(item())

prev = None  # guarantees compare False to all int's
sol = None
cnt = 0

for curr in items():
    curr = int(curr)
    if prev == curr:
        cnt += 1
    else:
        cnt = 1
        prev = curr
    if cnt == n and sol is None:
        sol = curr

if sol is None:
    print("No plateau of length " + str(n) + " occurs.")
else:
    print("A plateau of " + str(sol) + "'s of length at least " + str(n) + " occurs.")
