"""
Author: Jose Luis Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)
Start date: Germinal 2022.

Very simple tokenizer for stdin and similar objects. Finds toks
(simple tokens white-space separated); ends of line are counted
as white space but are otherwise ignored. 

Provides: 
- get_tok() that obtains the next tok and 
- iterator get_toks() on which to run a for loop to traverse all toks. 
Both combine naturally. Programmed using lexical closure strategy.
"""


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

if __name__ == "__main__":
    "example usages"
    print("Please write some lines and end with a line containing only control-D:")
    print("First word of first line was:", get_tok()) 
    "can be casted as int or float when/as necessary"
    print("Then comes the rest of the lines.")
    for w in get_toks():
        "traverse rest of stdin"
        print(w)
    print("\n\nNow with another iterable made of splittable strings,")
    g = [ "10 11 12", "13 14", "15 16 17 18" ]
    print("namely:", g)
    get_toks, get_tok = make_get_toks(g) # new variant to traverse g
    for w in get_toks():
        "see how we can mix them up"
        print("\nvar at for get_toks() loop:", w)
        print("get_tok() within for:", get_tok())
        print("again get_tok() within for:", get_tok())
