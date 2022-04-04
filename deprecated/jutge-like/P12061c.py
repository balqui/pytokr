'''
Based on submission S016, use pytokr
'''


from pytokr import get_tok, get_toks

s = get_tok()
while s != "beginning" and s != "end" and s is not None:
    s = get_tok()

if s != "beginning":
    print("wrong sequence")

else:
    n = 0
    wrong = True
    for s in get_toks():
        if s == "end":
            print(n)
            wrong = False
        n = n + 1
    if wrong:
        print("wrong sequence")
