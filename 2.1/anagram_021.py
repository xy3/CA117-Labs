import sys

def anagram(words):
	w1, w2 = list(words[0].lower()), list(words[1].lower())
	w1.sort()
	w2.sort()
	return w1 == w2

def main():
	for line in sys.stdin:
		print(anagram(line.rstrip().split()))

if __name__ == '__main__':
	main()

#depp