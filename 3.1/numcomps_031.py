import sys

def mult3(n):
	return [nm for nm in range(1, n+1) if not nm % 3]

def mult3sq(n):
	return [nm*nm for nm in range(1, n+1) if not nm % 3]

def mult4db(n):
	return [nm+nm for nm in range(1, n+1) if not nm % 4]

def mult3r4(n):
	return [nm for nm in range(1, n+1) if not nm % 4 or not nm % 3]

def mult3a4(n):
	return [nm for nm in range(1, n+1) if not nm % 4 and not nm % 3]

def multno3(n):
	return [remove3(nm) for nm in range(1, n+1)]

def remove3(n):
	if not n % 3:
		return 'X'
	else: return n

def primes(n):
	return [nm for nm in range(2, n+1) if is_prime(nm)]

def is_prime(a):
    return all(a % i for i in range(2, a))

def main():
	n = int(sys.argv[1])
	print("Multiples of 3: {}".format(mult3(n)))
	print("Multiples of 3 squared: {}".format(mult3sq(n)))
	print("Multiples of 4 doubled: {}".format(mult4db(n)))
	print("Multiples of 3 or 4: {}".format(mult3r4(n)))
	print("Multiples of 3 and 4: {}".format(mult3a4(n)))
	print("Multiples of 3 replaced: {}".format(multno3(n)))
	print("Primes: {}".format(primes(n)))

if __name__ == '__main__':
	main()