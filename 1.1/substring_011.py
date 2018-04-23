import sys

def mid(s):
	s = s.split()
	a = s[0].lower()
	b = s[1].lower()
	if a in b:
		return True
	else:
		return False

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		print(mid(l))

if __name__ == '__main__':
	main()