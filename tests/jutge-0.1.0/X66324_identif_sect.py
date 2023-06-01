from pytokr import pytokr

item, items = pytokr(iter = True)

for a in items():
    a = int(a)
    b, n = int(item()), int(item())
    s = list()
    c = "no"
    for _ in range(n):
        v = int(item())
        if c == "yes" and v == b:
            c = "done"
        elif c == "yes":
            s.append(v)
        elif c == "no" and v == a:
            c = "yes"
    if c == "done":
        for e in s:
            print(e, end = ' ')
    print()
    print('-' * 10)
