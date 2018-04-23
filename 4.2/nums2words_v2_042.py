import sys

nums = {
("zero", "naid"): "0",
("one", "aon"): "1",
("two", "do"): "2",
("three", "tri"): "3",
("four", "ceathar"): "4",
("five", "cuig"): "5",
("six", "se"): "6",
("seven", "seacht"): "7",
("eight", "ocht"): "8",
("nine", "naoi"): "9",
("ten", "deich"): "10",
}


zero 
one 
two 
three 
four 
five 
six 
seven 
eight 
nine 
ten 

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