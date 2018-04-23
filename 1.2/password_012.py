import sys

def pw(password):
	[d,l,u,s] = 0,0,0,0
	for char in password:
		if char.isdigit(): d = 1
		elif char.islower(): l = 1
		elif char.isupper(): u = 1
		else: s = 1
	print(sum([d,l,u,s]))

def main():
	for l in sys.stdin.readlines():
		l = l.strip()
		pw(l)

if __name__ == '__main__':
	main()