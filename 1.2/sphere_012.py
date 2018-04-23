import sys
from math import pi

def spherify(n):
	irad = n[0]
	incr = n[1]
	maxr = n[2]

	print("Radius (m)      Area (m^2)    Volume (m^3)")
	print("----------      ----------    ------------")
	i = irad
	while i < (maxr+incr):
		area = 4*pi*i**2
		volu = 4/3 * pi * i**3
		print("{:>10}".format(i)+"{:>16.2f}".format(area)+"{:>16.2f}".format(volu))
		i += incr

def main():
	n = sys.argv[1:]
	n = [float(x) for x in n]
	spherify(n)

if __name__ == '__main__':
	main()