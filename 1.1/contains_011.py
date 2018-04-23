import sys

def contains(s):
	result = True
	s = s.split()
	a = s[0].lower()
	b = s[1].lower()

	for char in a:
		if char in b:
			b = b.replace(char, "")
		else:
			result = False
	return result

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		print(contains(l))

if __name__ == '__main__':
	main()