import sys

def main():
	for line in sys.stdin:
		try:
			a,b,c = map(int, line.strip().split())
			r1 = ((-b) + ((b**2) - (4 * a * c))**0.5)/(2*a)
			r2 = ((-b) - ((b**2) - (4 * a * c))**0.5)/(2*a)

			if isinstance(r1, complex) or isinstance(r2, complex):
				print(None)
			else:
				print("r1 = {}, r2 = {}".format(r1, r2))

		except ValueError as e:
			if 'invalid literal' in str(e):
				pass
			elif TypeError:
				print(None)
			else:
				print(None)

if __name__ == '__main__':
	main()