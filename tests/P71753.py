

from tokr import get_tok

more = True
while more:
    try:
        n = int(get_tok())
        m = int(get_tok())
        for _ in range(n-1):
            p = int(get_tok())
            if p > m:
                m = p
        print(m)
    except StopIteration:
        more = False
	
