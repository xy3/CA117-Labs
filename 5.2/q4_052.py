import sys 

def build_dictionary(dic):
	newdic = {}
	f = open(dic).readlines()
	for line in f:
		l = line.strip().split()
		newdic[str(" ".join(l[:-1]))] = int(l[-1])

	return newdic

def sorter(t):
	return t[1]

def main():
	f = sys.argv[1]
	dic = build_dictionary(f)

	pts = {}
	for line in sys.stdin:
		line = line.strip().split(',', 1)
		name = line[0]
		foods = line[1].split(',')

		total = [int(dic[food]) if food in dic else 100 for food in foods]

		pts[name] = sum(total)

	lstr = len(max(pts.keys(), key=len))
	lnum = len(max(map(str, pts.values()), key=len))

	for (k, v) in sorted(pts.items(), key=sorter):
	    print('{:>{}} : {:>{}}'.format(k, lstr, v, lnum))

if __name__ == '__main__':
	main()