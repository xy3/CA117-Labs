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

def print_numbers(line):
	wordlist = []
	for char in line:
		if char in nums:
			wordlist.append(nums[char])
		else:
			wordlist.append("unknown")
	print(" ".join(wordlist))
def main():
	for line in sys.stdin:
		print_numbers(line.strip().split())

if __name__ == '__main__':
    main()