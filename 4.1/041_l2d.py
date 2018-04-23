dic = {}
def l2d(ls):
	for line in ls:
		l = line.strip().split()
		dic[l[0]] = l[1:]
	return dic