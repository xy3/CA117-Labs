import sys

punc = [',','.','/','[',']','!','*','&','^','@','?']

def main():
	s = sys.stdin.read().lower()
	for char in punc:
		s = s.replace(char, '')

	s = s.split()
	a = set([w.strip() for w in s])

	newlist = []

	for word in a:
		newlist.append("{} : {}".format(word, s.count(word)))

	for a in sorted(newlist):
		print(a)

if __name__ == '__main__':
	main()
