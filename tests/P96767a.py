

from tokr import get_tok, get_toks

x = float(get_tok())
x_pow = 1
r = 0

for coef in get_toks():
    r += x_pow*float(coef)
    x_pow *= x

print('{:.4f}'.format(r))
