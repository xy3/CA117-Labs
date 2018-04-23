import sys

def check_sorted(s):
	if "".join(sorted(s)) == s:
		return True
	else:
		return False

def ax(word):
	ls = []
	j = 0
	while j < len(word):
		i = 1
		while i < len(word) and check_sorted(word[j:i]) == True:
			i += 1
		ls.append(word[j:i])
		j += 1
	return ls


def main():
	strings = [n.strip() for n in sys.stdin.readlines()]
	for word in strings:
		axlw = ax(word)
		nl = []
		for w in axlw:
			if "".join(sorted(w)) != w:
				w1 = w[:-1]
				if "".join(sorted(w1)) != w1:
					w1 = w[1:]
			else:
				w1 = w
			nl.append(w1)
		 # = [w if ("".join(sorted(w)) == w for w in ax(word)]
		# print(max(nl, key=len))
		print(max(nl, key=len))

if __name__ == '__main__':
	main()