import sys

def chop(s):
	return s[1:-1]

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		if chop(l):
			print(chop(l))

if __name__ == '__main__':
	main()