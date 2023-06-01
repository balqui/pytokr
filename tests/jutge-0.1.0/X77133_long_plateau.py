from pytokr import pytokr

item, items = pytokr(iter = True)

n = int(item())

prev = None  # guarantees compare False to all int's
sol = None
cnt = 0

for curr in items():
    curr = int(curr)
    if prev == curr:
        cnt += 1
    else:
        cnt = 1
        prev = curr
    if cnt == n and sol is None:
        sol = curr

if sol is None:
    print("No plateau of length " + str(n) + " occurs.")
else:
    print("A plateau of " + str(sol) + "'s of length at least " + str(n) + " occurs.")
