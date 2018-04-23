def power(n1, n2):
	if n2 == 0:
		return 1
	return n1 * power(n1, n2-1)