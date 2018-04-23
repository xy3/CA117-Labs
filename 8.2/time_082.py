class Time(object):

	def __init__(self, h=0, m=0, s=0):
		self.h, self.m, self.s = h, m, s
	
	def __eq__(self, t2):
		return (self.h, self.m, self.s) == (t2.h, t2.m, t2.s)

	def __gt__(self, t2):
		return self.time_to_seconds() > t2.time_to_seconds()

	def __add__(self, t2):
		m = (self.m + t2.m)
		s = (self.s + t2.s)
		h = ((self.h + t2.h) % 24) + m // 60
		return Time(h, m % 60, s % 60)

	def __iadd__(self, t2):
		self.h = (self.h + t2.h + ((self.m + t2.m) // 60)) % 24
		self.m = (self.m + t2.m) % 60
		self.s = (self.s + t2.s) % 60
		return self

	def __str__(self):
		return "The time is {:02d}:{:02d}:{:02d}".format(self.h, self.m, self.s)

	def time_to_seconds(self):
		return (self.h * 3600) + (self.m * 60) + (self.s)

	@classmethod
	def seconds_to_time(cls, s):
		h = (s // 3600) % 24
		m = (s // 60) % 60
		s = s % 60
		
		return cls(h, m, s)
