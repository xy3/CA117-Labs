import sys

ones=['zero','one','two','three','four','five','six','seven','eight','nine']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


def toword(num):
	if num < 10:
		return ones[num]
	elif num < 20:
		return teens[num%10]
	elif num < 100:
		ns = list(str(num))
		t, o = int(ns[0]), int(ns[1])
		if o == 0:
			return tens[t]
		else:
			return "{}-{}".format(tens[t], ones[o])
	else:
		return "one hundred"

def main():
	lines = sys.stdin.readlines()

	for line in lines:
		numlist = []
		nums = [int(num) for num in line.split()]
		for num in nums:
			numlist.append(toword(num))
		print(" ".join(numlist))

if __name__ == '__main__':
    main()