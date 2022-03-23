

from tokr import get_tok

def dig2(k):
	if k < 10:
		return '0' + str(k)
	else:
		return str(k)

h = int(get_tok())
m = int(get_tok())
s = int(get_tok())

s += 1

if s == 60:
	s = 0
	m += 1
if m == 60:
	m = 0
	h += 1
if h == 24:
	h = 0

print(dig2(h) + ":" + dig2(m) + ":" + dig2(s))
