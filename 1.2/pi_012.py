import sys
from math import pi

def rhubard(n):
	return "{:.{}f}".format(pi, n)

def main():
	n = sys.argv[1]
	print(rhubard(n))

if __name__ == '__main__':
	main()