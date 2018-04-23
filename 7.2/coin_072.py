import random

class Coin(object):
	def __init__(self, sideup='Heads'):
		self.sideup = sideup

	def flip(self):
		coin = random.randint(1,2)
		if coin == 1:
			self.sideup = 'Heads'
		else:
			self.sideup = 'Tails'

	def getstate(self):
		return self.sideup

	def __str__(self):
		return 'Current state : {}'.format(self.sideup)