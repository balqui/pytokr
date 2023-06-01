from pytokr import pytokr

item, items = pytokr(iter = True)

a, b = int(item()), int(item())
c = "no"
m = None

for v in items():
    v = int(v)
    if c == "yes" and v == b:
        c = "done"
        break
    elif c == "yes" and (m is None or v > m):
        m = v
    elif c == "no" and v == a:
        c = "yes"

if c == "done" and m is None:
    print("empty section")
elif c == "done":
    print(f"maximum is: {m}")
else:
    print("nonexistent section")
