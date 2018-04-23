import sys

punc = [',','.','/','[',']','!','*','&','^','@','?', '-', '_']

def main():
	s = sys.stdin.read().lower()
	for char in punc:
		s = s.replace(char, '')

	s = s.split()
	a = set([w.strip() for w in s])

	newlist = []

	dw = 0
	ndw = 0
	for word in a:
		sc = s.count(word)
		
		if sc >= 3 and len(word) > 3:
			newlist.append("{} {}".format(word, sc))

			if len(str(sc)) > ndw : ndw = len(str(sc))
			if len(word) > dw: dw = len(word)

	for a in sorted(newlist):
		a = a.split()
		print('{:>{:d}s} : {:>{:d}s}'.format(a[0], dw, a[1], ndw))

if __name__ == '__main__':
	main()