import sys

def mid(s):
	return s[int(len(s)/2)]

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		if len(l)%2 != 0:
			print(mid(l))
		else: print("No middle character!")

if __name__ == '__main__':
	main()