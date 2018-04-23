class Triathlete(object):
	def __init__(self, name, tid):
		self.name, self.tid = name, tid
	
	def __str__(self):
		return "Name: {}\nID: {}".format(self.name, self.tid)