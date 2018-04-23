class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def reflect(self):
		self.x = -1 * self.x
		self.y = -1 * self.y

	def distance(self, p2):
		return ((((p2.x - self.x)**2)+((p2.y - self.y)**2))**0.5)