import sys

def nicer(words):
	i = 0
	while i < len(words):
		w = words[i]
		words[i] = w.capitalize()
		i += 1
	return words

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		l = l.split()
		print(" ".join(nicer(l)))

if __name__ == '__main__':
	main()