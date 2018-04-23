import sys

def vow(s):
	a = []
	for char in s:
		if char in "aeiou":
			a.append(char)
	return "".join(a)

def main():
	for s in sys.stdin:
		if vow(s.strip().lower()) == "aeiou":
			print(s.strip())

if __name__ == '__main__':
	main()