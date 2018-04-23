mport sys

vowels = ['a','e','i','o','u']
dicf = {}

def main():
        s = sys.stdin.read().lower()

        newlist = []
        for v in vowels:
                newlist.append("{} : {}".format(v, s.count(v)))

        print(newlist)

if __name__ == '__main__':
        main()
Import sys

vowels = ['a','e','i','o','u']
dicf = {}

def main():
	s = sys.stdin.read().lower()

	newlist = []
	for v in vowels:
		newlist.append("{} : {}".format(v, s.count(v)))

	print(newlist)

if __name__ == '__main__':
	main()
