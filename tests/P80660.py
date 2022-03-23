from sys import stdin

def get_toks(f = stdin):
    for line in f:
        for word in line.split():
            yield word



def collatz_next(n):
	'''
	Returns number following n in the Collatz sequence
	>>> collatz_next(5)
	16
	>>> collatz_next(16)
	8
	>>> collatz_next(13)
	40
	'''
	if n % 2 == 1:
		return 3 * n + 1
	else:
		return n//2

for data in get_words():
	c = 0
	n = int(data)
	while n != 1:
		n = collatz_next(n)
		c += 1
	print(c)
