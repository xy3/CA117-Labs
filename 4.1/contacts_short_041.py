import sys

dic = {}

def createdic(file):
	for s in file:
		s = s.strip().split()
		dic[s[0]] = s[1]

def listcontacts(line):
	line = line.strip()
	if line in dic:
		print('Name: {}\nPhone: {}'.format(line, dic[line]))
	else:
		print('Name: {}\nNo such contact'.format(line))

def main():
	f = open(sys.argv[1], 'r')
	createdic(f)

	for line in sys.stdin:
		listcontacts(line.strip())

if __name__ == '__main__':
	main()