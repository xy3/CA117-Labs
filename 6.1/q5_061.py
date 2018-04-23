import sys

def s_or_f(nums):
	try:
		total = sum([int(n) for n in nums.split()])
		return total
	except ValueError:
		return "False"

def sorter(score):
	return int(score.split(": ")[1])

def main():
	lines = [n.strip() for n in sys.stdin]
	scores = [(n.split(": ")[0] + ": " + str(s_or_f(n.split(": ")[1]))) for n in lines if s_or_f(n.split(": ")[1]) != "False"]

	mx_s = len(max([n.split(": ")[0] for n in scores], key=len))
	mx_n = len(max([n.split(": ")[1] for n in scores], key=len))

	scores = sorted(scores, key=sorter, reverse=True)
	for score in scores:
		s = score.split(": ")
		print("{:>{}}: {:>{}} points".format(s[0], mx_s, s[1], mx_n))

if __name__ == '__main__':
	main()