# pytokr

Very simple, somewhat stoned tokenizer for teaching purposes.

Behaviorally inspired by the early versions of the 
[easyinput module](https://github.com/jutge-org/easyinput); 
shares with it some similar aims, but not the aim of 
conceptual consistency with C/C++. Actually easyinput 
has grown in ways I find inappropriate for many of my 
students and I want to try now a different road.

## Install

Not pip-ready yet. Download or clone, then put the pytokr
folder where Python can see it from wherever you want to use it.

Plan is to offer it through pip at some point in the future.

## Simplest usage

Finds items (simple tokens white-space separated) in a 
string-based iterable such as stdin (default). Ends of 
line are counted as white space but are otherwise ignored. Usage:

`from pytokr import item, items`

(or only one of them as convenient). Then `item()` will provide
the next item in `stdin` and `for w in items()` will iterate on
whatever remains there. Calling `item()` at end of file will
raise an exception.

Both combine naturally: it is valid to call `item()` within 
a `for w in items()` loop provided there is still at least 
one item not yet read. The reading will advance on and the 
next item in the loop will correspond to the advance.

All items provided are of type `str` and will not contain 
white space; casting into `int` or `float` or whatever, if
convenient, falls upon the caller.

## Example

Based on [Jutge problem P29448](https://jutge.org/problems/P29448_en)
Correct Dates (and removing spoilers):

    from pytokr import items, item
    for d in items():
        m, y = item(), item()
        if correct_date(int(d), int(m), int(y)):
            print("Correct Date")
        else:
            print("Incorrect Date")

## Usage on other string-based iterables

`from pytokr import make_tokr`

Then, if `g` is an iterable of strings such as an open
file or a list of strings, the call

`item, items = make_tokr(g)`

will provide adapted versions of `item` and `items` that
will read them in from `g` instead of from `stdin`.

## To do: 

- Make it pip-ready.

- Automatize a process that generates a jutge-testable 
source even if jutge does not have pytokr (or get it to
have pytokr).

- Sources in the 'jutge-like' folder may be using 
obsolete identifiers; don't look at them too much.

- Calling 'tokens' the items sounded bad to me, first, 
because of the simplicity of the case and, second, due 
to the early programming level of my target students. 
Calling them 'items' is suboptimal though, since we are 
going to study `dict`'s later on and risk confusions. 
But I settled on 'items' for the time being anyway;
alternative suggestions welcome.
