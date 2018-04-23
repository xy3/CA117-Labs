import sys

def mean(nums):
	return sum(nums)/len(nums)

def median(nums):
	nums = sorted(nums)
	half = len(nums)//2

	if len(nums)%2 != 0:
		return float(nums[half])
	else:
		n1, n2 = nums[half-1], nums[half]
		return float((n1+n2)/2)

def main():
	nums = [int(n.strip()) for n in sys.stdin.readlines()]
	print("Mean: {:.1f}".format(mean(nums)))
	print("Median: {:.1f}".format(median(nums)))

if __name__ == '__main__':
	main()