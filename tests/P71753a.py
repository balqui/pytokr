

from tokr import get_tok, get_toks

for n in get_toks():
    m = int(get_tok())
    for i in range(int(n)-1):
        p = int(get_tok())
        if p > m:
            m = p
    print(m)
	
