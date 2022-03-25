

from pytokr import get_tok, get_toks

def leapyear(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def corrdate(d, m, y):
    return (m in range(1, 13) and 
           (d in range(1, 31) and m in (4, 6, 9, 11) or
            d in range(1, 32) and m in (1, 3, 5, 7, 8, 10, 12) or
            d in range(1, 29) and m == 2 or
            d == 29 and m == 2 and leapyear(y)))


for d in get_toks():
    m, y = get_tok(), get_tok()
    if corrdate(int(d), int(m), int(y)):
        print("Correct Date")
    else:
	    print("Incorrect Date")
