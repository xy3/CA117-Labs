import sys

def poemify(line, longest):
	return "{:^{}}".format(line, longest)

def main():
	poem = sys.stdin.readlines()
	longest = len(max(poem, key=len))-1
	for line in poem:
		print(poemify(line.strip(), longest))

if __name__ == '__main__':
	main()