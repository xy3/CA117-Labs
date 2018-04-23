import sys

file = [s.strip() for s in sys.stdin.readlines()]

def countsecs(time):
	t = time.split(":")
	try:
		return int(t[0])*60 + int(t[1])
	except:
		return "Fail"

def main():
	names = []
	mintimes = []
	timelist = []
	
	for line in file:
		times = line.split()[1:]
		
		timelist = [countsecs(time) for time in times]

		if "Fail" not in timelist:
			names.append(line.split()[0])
			# print(min(times, key=countsecs))
			mintimes.append(min(times, key=countsecs))

	person = names[mintimes.index(min(mintimes, key=countsecs))]
	mint = min(mintimes, key=countsecs)
	print("{} : {}".format(person, mint))

if __name__ == '__main__':
	main()