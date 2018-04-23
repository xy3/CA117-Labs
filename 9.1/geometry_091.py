class Point(object):
	def __init__(self, x, y):
		self.x, self.y = x, y

	def distance(self, p2):
		x2 = self.x - p2.x
		y2 = self.y - p2.y

		return float((x2 ** 2 + y2 ** 2) ** (1 / 2))


class Shape(object):
	def __init__(self, lp):
		self.points = lp

	def sides(self):
		length = [self.points[i].distance(self.points[i + 1]) for i in range(0, len(self.points) - 1)]
		length.append(self.points[-1].distance(self.points[0]))
		return length

	def perimeter(self):
		return sum(self.sides())


class Triangle(Shape):
	def area(self):
		sides = self.sides()
		s = sum(sides) / 2

		return (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** (1 / 2)


class Square(Shape):
	def area(self):
		return self.sides()[0] ** 2