'''
Submission S016 AC
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
    while s != "end" and s is not None:
        n = n + 1
        s = read(str)
    if s == "end":
        print(n)
    else:
        print("wrong sequence")
