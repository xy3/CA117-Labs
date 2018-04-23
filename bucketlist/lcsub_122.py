import sys

def go(s1, s2):
	largestrings = []
	i = 0
	while i < len(s1)-1:
		if s1[i:i+2] in s2:
			largestrings.append(s1[i:i+2])
		i += 1
	print(largestrings)
	j = 2
	while len(largestrings) > 1:
		for ls in largestrings:
			ix = s1.index(ls)
			lx = largestrings.index(ls)
			if s1[ix:ix + j] in s2:
				largestrings[lx] = s1[ix:ix + j]
			else:
				largestrings.pop(lx)
		j += 1

	string = str(largestrings[0])
	return "{} {} {}".format((string), len(string), s2.index(string))

def main():
	s1 = input().strip()
	s2 = input().strip()
	print(go(s1, s2))

if __name__ == '__main__':
	main()