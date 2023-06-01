
from sys import stdin

def get_toks(f = stdin):
    for line in f:
        for word in line.split():
            yield word

def make_get_tok(f = stdin):
	return iter(get_toks(f)).__next__

get_tok = make_get_tok()

