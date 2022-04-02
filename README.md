# pytokr

Very simple, somewhat stoned tokenizer for teaching purposes.

Behaviorally inspired by the early versions of the 
[easyinput module](https://github.com/jutge-org/easyinput); 
shares with it some similar aims, but not the aim of 
conceptual consistency with C/C++. Actually easyinput 
has grown in ways I find inappropriate for many of my 
students and I want to try now a different road.

## Simplest usage

`from pytokr import item, items`

(or only one of them as convenient). Then `item()` will provide
the next item in `stdin` and `for w in items()` will iterate on
whatever remains there. Calling `item()` at end of file will
raise an exception.

It is valid to call `item()` within a `for w in items()` loop
provided there is still at least one item not yet read. The
reading will advance on and the next item in the loop will 
correspond to the advance.

All items provided are of type `str` and cannot cointain 
white space; casting into `int` or `float` or whatever, if
convenient, falls upon the caller.

## Example

Based on [Jutge problem P29448](https://jutge.org/problems/P29448_en)
Correct Dates (and removing spoilers):

`from pytokr import items, item

for d in items():

    m, y = item(), item()

    if correct_date(int(d), int(m), int(y)):

        print("Correct Date")

    else:

        print("Incorrect Date")`

## Usage on other string-based iterables

`from pytokr import make_tokr`

Then, if `g` is an iterable of strings such as an open
file or a list of strings, the call

`item, items = make_tokr(g)`

will provide adapted versions of `item` and `items` to
be obtained from `g`.

## To do: 

- Automatize a process that generates a jutge-testable 
source even if jutge does not have pytokr (or get it to
have pytokr).
