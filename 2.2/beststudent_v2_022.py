import sys

dic = {}

def best(line):
	line = line.rstrip().split(" ", 1)
	if line[0] not in dic:
		dic[int(line[0])] = line[1]

def main():
	try:
		with open(sys.argv[1], 'r') as file:
			for line in file:
				best(line)

		student = dic[max(dic.keys())]
		grade = max(dic.keys())
	except FileNotFoundError:
		print("The file {} could not be opened.".format(sys.argv[1]))
	except ValueError:
		print("Invalid mark {} encountered. Exiting.".format(line.rstrip().split(" ", 1)[0]))
	else:
		print("Best student: {}\nBest mark: {}".format(student, grade))

if __name__ == '__main__':
	main()