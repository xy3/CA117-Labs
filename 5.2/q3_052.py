def build_dictionary(dic):
	newdic = {}
	f = open(dic).readlines()
	for line in f:
		l = line.strip().split()
		newdic[l[0]] = int(l[1])

	return newdic

def extract_range(d, low, high):
	nd = {key: value for (key, value) in d.items() if (value >= low and value <= high)}
	return nd