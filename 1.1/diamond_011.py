import sys

def diamond(n):
	dlist = []
	x = n-1
	for i in range(n-1):
		line = "{:>{}}".format(("*"*(n-x)), n)
		print(line.replace("*", "* ").rstrip())
		x -= 1
	for i in range(n):
		line = "{:>{}}".format(("*"*(n-i)), n)
		print(line.replace("*", "* ").rstrip())
		x -= 1

def main():
	n = int(sys.argv[1])
	diamond(n)

if __name__ == '__main__':
	main()