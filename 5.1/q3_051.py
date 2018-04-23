import sys
from re import findall as fa

def main():
	for s in sys.stdin:
		print(max(fa(r"[A-Z]+", s), key=len))

if __name__ == '__main__':
	main()