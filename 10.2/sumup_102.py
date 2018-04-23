def sumup(x):
	if x == 0:
		return 0
	return x + sumup(x-1)