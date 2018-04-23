class Employee(object):
	def __init__(self, name, number):
		self.n, self.num = name, number
		self.w = 0

	def __str__(self):
		l = []
		l.append("Name: {}".format(self.n))
		l.append("Number: {}".format(self.num))
		l.append("Wages: {:.2f}".format(self.wages()))
		return "\n".join(l)

	def wages(self):
		return self.w / 52

class Manager(Employee):
	def __init__(self, name, number, wages):
		super().__init__(name, number)
		self.w = wages

	def __str__(self):
		return super().__str__()

	def wages(self):
		return self.w / 52

class AssemblyWorker(Employee):
	def __init__(self, name, number, hr, hs):
		super().__init__(name, number)
		self.hr, self.hs = hr, hs

	def __str__(self):
		return super().__str__()

	def wages(self):
		return self.hr * self.hs
		