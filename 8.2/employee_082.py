class Employee(object):

	next_employee_number = 0

	def __init__(self, name, employee_number=None, hourly_rate=9.25, hours_worked=0):
		self.nm = name
		if employee_number == None:
			self.en = Employee.next_employee_number
		else: self.en = employee_number
		self.hr = hourly_rate
		self.hw = hours_worked
		Employee.next_employee_number += 1
		
	def __str__(self):
		l = []
		l.append("Name: {}".format(self.nm))
		l.append("ID: {}".format(self.en))
		l.append("Hours: {:.2f}".format(self.hw))
		l.append("Rate: {:.2f}".format(self.hr))
		l.append("Wages: {:.2f}".format(self.hr * self.hw))
		return "\n".join(l)

	def add_hours(self, h):
		self.hw = self.hw + h
		return self
