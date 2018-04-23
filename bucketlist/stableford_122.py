import sys

def points(stroke, i, p, hcap):
	stroke = int(stroke) - hcap // 18
	if i <= hcap % 18: stroke -= 1
	return max(0, p - stroke + 2)

def insl(): return list(map(int, input().split()))

def kv(l):
	l = l.split()
	return (" ".join(l[:-19]), (l[-19], list(enumerate((l[-18:])))))

def main():
	pars, indexes = insl(), insl()
	lines = [l.strip() for l in sys.stdin.readlines()]
	names = [" ".join(line.split()[:-19]) for line in lines]
	players, d_plyrs = {kv(l)[0]: kv(l)[1] for l in lines}, []

	for item in players.items():
		score = 0
		try:
			for i, stroke in (item[1][1]):
				if stroke == "X": continue
				score += points(stroke, indexes[i], pars[i], int(item[1][0]))
			players[item[0]] = score
		except Exception:
			d_plyrs.append(item[0])

	for p in d_plyrs: del players[p]
	anames = d_plyrs + list(players.keys())
	mxl = len(max(anames, key=len))
	
	for n, s in sorted(players.items(), key=lambda x: x[1], reverse=True):
		print('{:>{}s} : {:>2}'.format(n, mxl, s))
	
	for n in names:
		if n in d_plyrs: print('{:>{}s} : {}'.format(n, mxl, "Disqualified"))

if __name__ == '__main__':
	main()