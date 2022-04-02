'''
Based on submission S016, try TLE
'''


from easyinput import read

s = read(str)
while s != "beginning" and s != "end" and s is not None:
    s = read(str)

if s != "beginning":
    print("wrong sequence")

else:
    n = 0
    s = read(str)
    wrong = True
    while s is not None:
        if s == "end":
            print(n)
            wrong = False
        n = n + 1
        s = read(str)
    if wrong:
        print("wrong sequence")
