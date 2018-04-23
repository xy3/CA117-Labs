def reverse_list(l):
	if len(l) == 0:
		return l
	l2 = reverse_list(l[1:])
	l2.append(l[0])
	return l2