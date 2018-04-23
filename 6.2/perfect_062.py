import sys

def sumFac(x):
	result = []
	i = 1
	while i*i <= x:
		if x % i == 0:
			result.append(i)
			if x/i != i:
				result.append(x/i)
		i += 1
	return result

def main():
	for x in sys.stdin:
		x = int(x)
		print(((sum(sumFac(x)) - x) == x))

if __name__ == '__main__':
	main()