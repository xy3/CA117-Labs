class Stack(object):
	def __init__(self):
		self.l = l

	def push(self, n):
		self.l.append(n)

	def is_empty(self):
		return len(self.l) == 0
	
	def pop(self):
		return self.l.pop()

	def top(self):
		return self.l[-1]

	def __len__(self):
		return len(self.l)