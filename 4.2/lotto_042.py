import random, time
from multiprocessing.dummy import Pool as ThreadPool 

pool = ThreadPool(4)

f = open("output.txt", "w+")

def main():
	t0 = time.time()
	
	lottery = (random.sample(range(1, 47), 6) for i in range(10**6))
	lotnums = [" ".join(str(x) for x in num) for num in lottery]
	
	f.write("\n".join(lotnums))

	# results = pool.map(generate, lottery)

	# pool.close()
	# pool.join()
	
	t1 = time.time()

	print(str(t1-t0))

if __name__ == '__main__':
	main()