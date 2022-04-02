"Idea: aim at too slow TLE; but first want a passing one, this fails empty sequences"

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


n = int(get_tok())

# prev = int(get_tok()) # Fails, statement does not promise at least one value

prev = None # guarantees compare False to all int's
cnt = 0

for curr in get_toks():
    curr = int(curr)
    if cnt < n:
        if prev == curr:
            cnt += 1
        else:
            cnt = 1
            prev = curr

if cnt == n:
    print("A plateau of " + str(prev) + "'s of length at least " + str(n) + " occurs.")
else:
    print("No plateau of length " + str(n) + " occurs.")


