class Student(object):
	def __init__(self, sn, fn, sid, ml=None):
		if ml == None:
			ml = []
		self.sn, self.fn, self.sid, self.ml = sn, fn, str(sid), ml

	def add_module(self, module):
		if module not in self.ml:
			self.ml.append(module)

	def del_module(self, module):
		if module in self.ml:
			self.ml.remove(module)

	def print_details(self):
		print('ID: ' + self.sid)
		print('Surname: ' + self.sn)
		print('Forename: ' + self.fn)
		print('Modules: ' + " ".join(self.ml))