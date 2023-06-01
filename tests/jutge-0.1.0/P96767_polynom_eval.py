from pytokr import pytokr

item, items = pytokr(iter = True)


x = float(item())
x_pow = 1
r = 0

for coef in items():
    r += x_pow * float(coef)
    x_pow *= x

print('{:.4f}'.format(r))
