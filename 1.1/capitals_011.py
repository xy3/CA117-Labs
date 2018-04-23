import sys

def cap(fs,ls):
	return fs.upper(), ls.upper()

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		if len(l) > 1:
			fs = l[0]
			ls = l[-1]
			lts = cap(fs,ls)
			word = lts[0] + l[1:-1] + lts[1]
			print(word)

if __name__ == '__main__':
	main()