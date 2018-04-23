import sys

dic = {	0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}

names = [
	"nothing",
	"one pair",
	"two pairs",
	"three of a kind",
	"a straight",
	"a flush",
	"a full house",
	"four of a kind",
	"a straight flush",
	"a royal flush"
	]

def poker(cards):
	dic[int(cards[-1])] += 1

def main():
	total = 0
	for line in sys.stdin:
		poker(line.rstrip())
		total += 1
	x = 0
	for num in dic:
		print("The probability of {} is {:.4f}%".format(names[x], ((dic[num]/total)*100)))
		x += 1

if __name__ == '__main__':
	main()