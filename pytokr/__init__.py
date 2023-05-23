"""
Author: Jose Luis Balcazar, ORCID 0000-0003-4248-4528, balqui at GitHub
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)
Start date: Germinal 2022.

This source: version 0.1.1.

Very simple tokenizer for stdin and similar objects. Finds items
(simple tokens white-space separated) in a string-based iterable
such as stdin (default). Ends of line are counted as white space 
but are otherwise ignored. 

Provides a function pytokr() that returns: 
- a function (formerly called item()) that obtains the next item and 
- if required, an iterator (formerly called items()) on which one can 
  run a for loop to traverse all the items.
The returned values of pytokr() may get whatever names the user want.

Both combine naturally: the individual item function can be called 
inside the for loop of the iterator and this advances the items; 
so, the next item at the loop will be the current one after the 
local advances.

Token items are returned as strings; user should cast them as
int or float or whatever when appropriate.

Programmed using a lexical closure strategy.

Usage: for reading in items from stdin, just import item and/or
items; for usage on another string-based iterable, import and
call make_tokr.

Former usage: one could import
- item() that obtains the next item and 
- iterator items() on which one can run a for loop to traverse 
all the items.
- make_tokr() to create tailored versions of these function and 
iterator.
This usage is still possible but will send a deprecation warning
through stderr.
"""

def pytokr(f = None, /, also_iter = False):
    '''
    make iterator and next functions out of iterable of split strings
    return next function and, if requested, iterator too
    '''

    from itertools import chain

    def the_it():
        "so that both outcomes are called with parentheses"
        return it

    if f is None:
        from sys import stdin as f
    it = chain.from_iterable(map(str.split, f))
    if also_iter:
        return it.__next__, the_it
    return it.__next__

# everything below is unnecessary
# and kept only for partial compatibility with earlier versions:
# functions work but will print a deprecation warning through stderr

def make_tokr(f = None, /, internal_call = False):
    '''
    make iterator and next functions out of iterable of split strings
    deprecated usage - import pytokr instead, see https://github.com/balqui/pytokr
    Param internal_call for appropriate deprecation reporting
    '''
    from sys import stderr # for deprecation warning

    from itertools import chain
    
    depr_reported = False

    def the_it():
        '''
        additional usage for deprecation reporting
        '''
        def depr_it():
            nonlocal depr_reported
            if internal_call and not depr_reported:
                "user imported item, items, report deprecation once"
                print("[stderr] Functions items, item, make_tokr are deprecated;",
                        file = stderr, end = " ")
                print("please see https://github.com/balqui/pytokr", file = stderr)
            depr_reported = True
            return it
        return depr_it()

    def the_it_next():
        '''
        so that both, items and item, are called with parentheses,
        additional usage for deprecation reporting.
        '''
        def depr_it():
            nonlocal depr_reported
            if internal_call and not depr_reported:
                "user imported item, items, report deprecation once"
                print("[stderr] Functions item, items, make_tokr are deprecated;",
                        file = stderr, end = " ")
                print("please see https://github.com/balqui/pytokr", file = stderr)
            depr_reported = True
            return it.__next__()
        return depr_it

    if not internal_call and not depr_reported:
        "user made its own tokr, report deprecation"
        print("[stderr] Functions make_tokr, item, items are deprecated;",
                file = stderr, end = " ")
        print("please see https://github.com/balqui/pytokr", file = stderr)
        depr_reported = True

    if f is None:
        from sys import stdin as f
    it = chain.from_iterable(map(str.split, f))
    return the_it, the_it_next() # it.__next__


items, item = make_tokr(internal_call = True)

if __name__ == "__main__":
    "example usages"
    item, items = pytokr(also_iter = True)
    print("Please write some lines and end with a line containing only control-D:")
    print("First word of first line was:", item()) 
    print("Then comes the rest of the lines.")
    for w in items():
        "traverse rest of stdin"
        print(w)
    print("\n\nNow with another iterable made of splittable strings,")
    g = [ "10 11 12", "13 14", "15 16 17 18" ]
    print("namely:", g)
    item, items = pytokr(g, also_iter = True) # new variant to traverse g
    for w in items():
        "see how we can mix them up"
        print("\nCurrent value of w at for w in items() loop:", w)
        print("item() grabbed within the loop:", item())
        print("another item() grabbed also within the loop:", item())
