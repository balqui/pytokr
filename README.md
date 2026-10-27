# pytokr

Very simple, somewhat stoned tokenizer for teaching purposes.

Behaviorally inspired by the early versions of the 
[easyinput module](https://github.com/jutge-org/easyinput); 
shares with it some similar aims, but not the aim of 
conceptual consistency with C/C++. A separate, different 
evolution of `easyinput` is [yogi](https://github.com/jutge-org/yogi).

## Install

The usual incantation should work: `pip install pytokr` or,
in case you already have an earlier `pytokr`,
`pip install --upgrade pytokr`
(maybe with either `sudo` or `--user` or within a 
virtual environment). You may need to call `pip` 
preceded by `python -m`. 

If that does not work, download or clone the repo, then 
put the `pytokr` folder where Python can see it from 
wherever you want to use it.

## Simplest usage

Finds items (simple tokens, white-space separated) in a 
string-based iterable such as stdin (default). Ends of 
line are counted as white space but are otherwise ignored. 

Simplest usage is

`from pytokr import item`

Then call `item()` to keep retrieving white-space-sparated
items from `stdin`. In case no items remain, a custom 
`EndOfDataError` exception will be raised. Note that, 
as white-space is ignored, including ends of line, 
in case only white-space remains then the program _is_ at 
end of data. The outcomes are `str`: casting them into 
`int` or `float` or whatever, if convenient, falls upon 
the caller. 
Of course you can assign to the function a different name
at `import` time by using a standard `as` clause.

Alternatively, you may import an iterator on the whole
contents of `stdin`:

`from pytokr import items`

It is most naturally employed in a `for` loop:

`for itm in items():`

Then, the iterator gracefully stops at end of data and 
does not raise the `EndOfDataError` exception. Again the
renaming option applies, of course, and again ends of line
are ignored as white space.

In case you import both, they will interact naturally: the 
individual `item()` function can be called inside a `for` 
loop on the iterator, provided there is still at least 
one item not yet read. That call will advance the items; 
so, the next item at the loop will be the current one _after_ 
the local advances. Briefly: both advance _the same_ iterator.

## Slightly less simple usage

Alternatively, import the function that creates the reading
functions:

`from pytokr import pytokr`

Call then `pytokr` to obtain the tokenizer function; give it 
whatever name you see fit, say, `item`:

`item = pytokr()`

If a different source of items is desired, say `source` 
(e.g. a `file` just `open`'ed or a list of strings), 
simply pass it on:

`item = pytokr(source)`

In either case, a second output can be requested, namely, an
iterator over the items, say you want to name it `items`:

`item, items = pytokr(iter = True)`

(such a call would accept as well a `source` as first parameter).
Then you can run `for itm in items():` or make up a `ls = list(items())`
and, with some care, avoid the dependence on the `EndOfDataError`
exception. Both combine naturally as explained above.

Also `from pytokr import __version__` works as expected.

## Example

Based on [Jutge problem P29448](https://jutge.org/problems/P29448_en)
Correct Dates (and removing spoilers):

    from pytokr import pytokr
    item, items = pytokr(iter = True)
    # alternative: from pytokr import item, items
    for d in items():
        m, y = item(), item()
        if correct_date(int(d), int(m), int(y)):
            print("Correct Date")
        else:
            print("Incorrect Date")

## (Un)Deprecations

The import of `item` and `items` has gone through several
deprecation and undeprecation stages. They are currently
undeprecated and usable with normality. Please try to upgrade
to the most advanced version of `pytokr` and check the descriptions above.

The function `make_tokr` from earlier versions stays
deprecated. If employed on the current version it will 
still work but will print a deprecation message on `stderr`.

