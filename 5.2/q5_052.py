import sys 

def sorter(t):
	return t[1]

def main():
	passed = {}
	failed = []
	
	for line in sys.stdin:
		line = line.strip().split(':')
		name = line[0]

		scores = line[1].split(',')

		try:
			passed[name] = sum(map(int, scores))
		except Exception:
			failed.append(name)

	for (k, v) in sorted(passed.items(), key=sorter, reverse=True):
	    print('{} : {}'.format(k, v))

	print('Skipped:')
	for p in failed:
		print(p)


if __name__ == '__main__':
	main()