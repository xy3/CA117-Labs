import sys

def qButNotU(wlist):
        return [word for word in wlist if quEstion(word.lower())]

def quEstion(word):
        return word.count('q') > word.count('qu')

def main():
	a = sys.stdin.read().split()
	print("Words with q but no u: {}".format(qButNotU(a)))

if __name__ == '__main__':
	main()