def maximum(l):
	if len(l) == 1 or l[0] > maximum(l[1:]):
		return l[0]
	return maximum(l[1:])