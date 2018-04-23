import sys

nums = {
"0": "zero",
"1": "one",
"2": "two",
"3": "three",
"4": "four",
"5": "five",
"6": "six",
"7": "seven",
"8": "eight",
"9": "nine",
"10": "ten"
}

transdic = {}

def print_numbers(line):
	wordlist = []
	for char in line:
		wordlist.append(transdic[nums[char]])
	print(" ".join(wordlist))

def importdic(pair):
	global transdic
	transdic[pair[0]] = pair[1]

def main():
	dicfile = open(sys.argv[1], "r")
	for line in dicfile:
		importdic(line.strip().split())
	dicfile.close()

	for line in sys.stdin:
		print_numbers(line.strip().split())

if __name__ == '__main__':
    main()