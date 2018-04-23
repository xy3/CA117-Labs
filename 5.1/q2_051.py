import sys

def evil(s):
	return "".join([char for char in s if char in "evil"])

def main():
	for s in sys.stdin:
		if evil(s.strip().lower()) == "evil":
			print(s.strip())

if __name__ == '__main__':
	main()