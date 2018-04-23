import sys

def worse(words):
	i = 0
	while i < len(words):
		i = 0
		while i < len(words):
			words[i] = words[i][::-1]
			words[i] = words[i].capitalize()
			words[i] = words[i][::-1]
			i += 1
	return words

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		l = l.split()
		print(" ".join(worse(l)))

if __name__ == '__main__':
	main()