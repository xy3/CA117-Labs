class PQ(object):
	def __init__(self):
		self.d = {}
		self.N = 0

	def is_empty(self): return self.N == 0
	def size(self): return self.N
	def getMax(self): return self.d[1]

	def insert(self, v):
		self.N += 1
		self.d[self.N] = v
		self.swim(self.N)

	def swp(self, i, j):
		self.d[i], self.d[j] = self.d[j], self.d[i]
	
	def swim(self, k):
		while k > 1 and self.d[k//2] < self.d[k]:
			self.swp(k, k//2)
			k = k//2

	def delMax(self):
		v = self.d[1]
		self.swp(1, self.N)
		del(self.d[self.N])
		self.N -= 1
		self.sink(1)
		return v

	def sink(self, k):
		stop = False
		while (k * 2 <= self.N) and stop == False:
			j = self.bgr(k * 2, (k * 2)+1)
			if self.d[k] >= self.d[j]: stop = True
			self.swp(k, j)
			k = j

	def bgr(self, i, j):
		try:
			return max([i, j], key=self.d.__getitem__)
		except KeyError:
			return i

	def check(self, number):
		if max(self.d.values()) > number:

			i = 1
			while self.d[i] != max(self.d.values()):
				i += 1

			self.d[i] = number
			self.swim(i) 

	def delmin(self):
		root = self.d[1]
		self.d[1], self.d[len(self.d)] = self.d[len(self.d)], self.d[1]
		
		del(self.d[self.p])
		self.p -= 1
		
		self.sink(1)
		return root 