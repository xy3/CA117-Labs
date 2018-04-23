class Score(object):
	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points
		self.score = (self.goals*3) + self.points
	
	def greater_than(self, sc2):
		if self.score > sc2.score:
			return True
		else:
			return False

	def less_than(self, sc2):
		if self.score < sc2.score:
			return True
		else:
			return False

	def equal_to(self, sc2):
		if self.score == sc2.score:
			return True
		else:
			return False