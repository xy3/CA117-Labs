import sys

def main():
	s = sys.argv[1].strip()
	n = int(sys.argv[2].strip())

	x = n % len(s)
	print(s[x:] + s[:x])

if __name__ == '__main__':
	main()