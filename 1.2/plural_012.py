import sys

a = ["ch", "sh", "x", "s", "z", "o"]
b = ["f", "fe"]
vowels = "aeiou"

def plural(word):
	if word.endswith(tuple(a)):
		return word+"es"
	for x in b:
		if word.endswith(x):
			return word[:0-(len(x))]+"ves"
	if word[-2] not in vowels and word.endswith("y"):
		return word[:-1]+"ies"
	else: return word+"s"

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		print(plural(l))

if __name__ == '__main__':
	main()