import sys

def isnum(line):
	if not line.isdigit():
		print("{} is not a number".format(line))
	else: 
		print("Thank you for {}".format(line))
		sys.exit()

def main():
	for line in sys.stdin:
		isnum(line.rstrip())

if __name__ == '__main__':
	main()