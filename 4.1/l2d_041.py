import sys

dic = {}
def l2d(ls):
	dl = ls.readlines()
	dl0 = dl[0].strip().split()
	dl1 = dl[1].strip().split()

	i = 0
	while i < len(dl0):
		dic[dl0[i]] = dl1[i]
		i += 1

	return dic

def main():
	l2d(sys.stdin)

if __name__ == '__main__':
	main()