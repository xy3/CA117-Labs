class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, p2):
		return (((p2.x - self.x)**2) + ((p2.y - self.y)**2))**0.5

	def __str__(self):
		return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment(object):
	def __init__(self, p1, p2):
		self.x1 = p1.x
		self.x2 = p2.x
		self.y1 = p1.y
		self.y2 = p2.y

	def midpoint(self):
		x1, x2, y1, y2 = self.x1, self.x2, self.y1, self.y2
		return Point((x2 + x1)/2, (y2 + y1)/2)

class Circle(object):
	def __init__(self, p, r):
		self.p = p
		self.r = r

	def overlaps(self, c2):
		return self.p.distance(c2.p) < (self.r + c2.r)
