class Weight(object):

	OUNCES_PER_POUND = 16

	def __init__(self, p=0, o=0):
		self.p, self.o = p, o

	def __str__(self):
		return "{} pound(s) and {} ounce(s)".format(self.p, self.o)

	def __eq__(self, w2):
		return self.total() == w2.total()
	def __ne__(self, w2):
		return self.total() != w2.total()
	def __lt__(self, w2):
		return self.total() < w2.total()
	def __gt__(self, w2):
		return self.total() > w2.total()
	def __ge__(self, w2):
		return self.total() >= w2.total()
	def __le__(self, w2):
		return self.total() <= w2.total()


	def __add__(self, w2):
		return self.from_ounces(self.total() + w2.total())
	
	def __iadd__(self, w2):
		wn = self + w2
		self.p, self.o = wn.p, wn.o
		return self

	def __mul__(self, n):
		return self.from_ounces(self.total() * n)

	def total(self):
		return (self.p * 16) + self.o

	@classmethod
	def from_ounces(cls, o):
		return cls(o//16, o%16)