import sys

def conv(numb, base):
	i = len(numb)-1
	x = 0
	total = 0
	while i >= 0:
		n = int(numb[i])
		total += n*(base**x)
		x+=1
		i-=1
	return total

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		numb = l.split()[0]
		base = int(l.split()[1])
		print(conv(numb, base))

if __name__ == '__main__':
	main()