import sys

def tablify(line, longest):
	line = line.split()
	name = " ".join(line[1:-8])
	
	x = "{:>3}".format(line[0])
	x += " {:<{}} ".format(name, longest)
	x += "{:^3}".format(line[-8])
	for item in line[-7:]:
		x += "{:>3} ".format(item)
	return x[:-1]

def main():
	leagues = sys.stdin.readlines()
	leagues.insert(0, "POS CLUB P W D L GF GA GD PTS")
	names = []
	
	for row in leagues:
		names.append(" ".join(row.split()[1:-8]))
	longest = len(max(names, key=len))
	
	for line in leagues:
		print(tablify(line.rstrip(), longest))

if __name__ == '__main__':
	main()