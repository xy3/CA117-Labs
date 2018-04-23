import sys

def maxscore(a, b, c, x):
	hscore, a_add = 0, x
	while a_add >= 0:
		b_add = x - a_add
		while b_add >= 0:
			c_add = x - (a_add + b_add)

			ntokens = [a + a_add, b + b_add, c + c_add]

			score = sum(map(lambda x: x**2, ntokens)) + (min(ntokens) * 7)
			if score > hscore: hscore, htokens = score, ntokens

			b_add -= 1
		a_add -= 1

	return hscore#, htokens

def main():
	for line in sys.stdin:
		a, b, c, x = map(int, line.strip().split())
		print(maxscore(a, b, c, x))

if __name__ == '__main__':
	main()