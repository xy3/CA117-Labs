class Triathlete(object):
	def __init__(self, name, tid):
		self.times = {'swim' : 0, 'cycle' : 0, 'run' : 0}
		self.total = 0
		self.name, self.tid = name, tid
	
	def __str__(self):
		return ("Name: {}\n" +
				"ID: {}\n" +
				"Race time: {}"
				).format(self.name, self.tid, self.total)

	def __gt__(self, t2):
		return self.total > t2.total
	def __lt__(self, t2):
		return self.total < t2.total
	def __eq__(self, t2):
		return self.total == t2.total

	def add_time(self, dis, time):
		self.times[dis] = time
		self.total = sum(self.times.values())

	def get_time(self, dis):
		return self.times[dis]

