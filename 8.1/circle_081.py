class Point(object):
	def __init__(self, x=0, y=0):
		self.x, self.y = x, y

	def __str__(self):
		return "({:.1f}, {:.1f})".format(self.x, self.y)

	def midpoint(self, p2):
		x1, y1, x2, y2 = self.x, self.y, p2.x, p2.y
		return Point((x2 + x1)/2, (y2 + y1)/2)

class Circle(object):
	def __init__(self, p, r):
		self.p, self.r = p, r
	
	def __add__(self, c2):
		self.p = self.p.midpoint(c2.p)
		self.r = self.r + c2.r
		return (self)

	def __str__(self):
		return "Centre: {}\nRadius: {}".format(self.p, self.r)