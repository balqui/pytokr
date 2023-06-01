from pytokr import pytokr

item, items = pytokr(iter = True)

lim = int(item())

from collections import defaultdict as dd

frq = dd(int)
m = set()

for w in items():
	"add here at some point the early exit before Jutge testing"
    frq[w] += 1
    if frq[w] >= lim and w not in m and len(m) < 2:
        m.add(w)
if len(m) < 2:
    print(f'Less than two words appear {lim} or more times.')
else:
    print(f'There are two words that appear {lim} or more times.')
