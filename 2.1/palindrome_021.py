import sys

def palindrome(line):
	line = line.lower()
	for char in line:
		if not char.isalnum():
			line = line.replace(char, "")
	return line[::-1] == line

def main():
	for line in sys.stdin:
		print(palindrome(line.rstrip()))

if __name__ == '__main__':
	main()