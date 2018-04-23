import sys
import string

a = []

def depunctify(line):
	line = line.lower()
	for char in line:
		if char in string.punctuation:
			line = line.replace(char, "")
	for word in line.split():
		if word not in a:
			a.append(word)

def main():
	for line in sys.stdin:
		depunctify(line.rstrip())
	print(len(a))

if __name__ == '__main__':
	main()