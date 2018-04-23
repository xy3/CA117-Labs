import sys

file = [int(s.strip()) for s in sys.stdin.readlines()]

def rcount(s):
	return file.count(s)

def median(lst):
	n = len(lst)
	if n % 2 == 1:
		return sorted(lst)[n//2]
	else:
		return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def main():
	l = len(file)

	mean = (sum(file))/l
	mode = max(file, key=rcount)
	# median = int(sorted(list(file))[(l//2)])
	med = median(file)
	
	print("Mean: {:.1f}".format(mean))
	print("Mode: {:.1f}".format(mode))
	print("Median: {:.1f}".format(med))

if __name__ == '__main__':
	main()