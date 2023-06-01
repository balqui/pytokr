from pytokr import pytokr

item, items = pytokr(iter = True)

lim = int(item())

from collections import defaultdict as dd

frq = dd(int)
m = None

for w in items():
    frq[w] += 1
    if frq[w] > lim and m is None:
        m = w
if m is None:
    print(f'No words reach above frequency {lim}.')
else:
    print(f'The first word to reach above frequency {lim} is "{m}".')
