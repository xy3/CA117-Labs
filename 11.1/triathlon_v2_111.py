class Triathlete(object):
	def __init__(self, name, tid):
		self.times = {'swim' : 0, 'cycle' : 0, 'run' : 0}
		self.total = 0
		self.name, self.tid = name, tid
	
	def __str__(self):
		return ("Name: {}\n" +
				"ID: {}"
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

class Triathlon(object):
	def __init__(self):
		self.ts = {}

	def __str__(self):
		return '\n'.join(map(str, sorted(self.ts.values(), key=self.sortn)))
	
	def sortn(self, t):
		return t.name

	def sortt(self, t):
		return t.total

	def best(self):
		return str(min(self.ts.values(), key=self.sortt))

	def add(self, t):
		self.ts[t.tid] = t

	def lookup(self, tid):
		if tid in self.ts:
			return self.ts[tid]
		else: return None

	def remove(self, tid):
		del(self.ts[tid])

		