import sys

def count(line):
	return len(line.split())

def main():
	total = 0
	for line in sys.stdin:
		total += count(line.rstrip())
	print(total)

if __name__ == '__main__':
	main()