class Score(object):
	def __init__(self, goals=0, points=0):
		self.goals, self.points = goals, points
		self.ts = ((self.goals * 3) + self.points)
	
	def __str__(self):
		return "{} goal(s) and {} point(s)".format(self.goals, self.points)

	def __eq__(self, s2):
		return self.ts == s2.ts

	def __gt__(self, s2):
		return self.ts > s2.ts

	def __lt__(self, s2):
		return self.ts < s2.ts

	def __le__(self, s2):
		return self.ts <= s2.ts

	def __ge__(self, s2):
		return self.ts >= s2.ts

	def __add__(self, s2):
		g = self.goals + s2.goals
		p = self.points + s2.points
		return Score(g,p)

	def __sub__(self, s2):
		g = self.goals - s2.goals
		p = self.points - s2.points
		return Score(g,p)

	def __iadd__(self, s2):
		self.goals += s2.goals
		self.points += s2.points
		return self

	def __isub__(self, s2):
		self.goals -= s2.goals
		self.points -= s2.points
		return self

	def __mul__(self, n):
		g = n * self.goals
		p = n * self.points
		return Score(g,p)

	def __rmul__(self, n):
		g = n * self.goals
		p = n * self.points
		return Score(g,p)

	def __imul__(self, n):
		self.goals *= n
		self.points *= n
		return self