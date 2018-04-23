import sys

def flip(s):
	return ''.join([s[x:x+2][::-1] for x in range(0, len(s), 2)])

def main():
	s = sys.argv[1]
	print(flip(s))

if __name__ == '__main__':
	main()