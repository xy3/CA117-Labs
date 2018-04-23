from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
			   'CA106': Module('CA106', 'Web Design', 5),
			   'CA115': Module('CA115', 'Digital Innovation', 5),
			   'CA116': Module('CA116', 'Computer Programming I', 10),
			   'CA117': Module('CA117', 'Computer Programming II', 10),
			   'CA169': Module('CA169', 'Networks and Internet', 5),
			   'CA170': Module('CA170', 'Operating Systems', 5),
			   'CA172': Module('CA172', 'Problem Solving', 5),
			   'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

	def __init__(self, idnum, surname, firstname):
		self.idnum = idnum
		self.surname = surname
		self.firstname = firstname
		self.mods = CA1_MODULES
		self.marks = {code: 0 for code in self.mods.keys()}
		self.pm = 0

	def __str__(self):
		# return str(self.precision_mark())
		name = '{} : {} {}'.format(self.idnum,
		                           self.firstname,
		                           self.surname)
		uline = '-' * len(name)
		results =  '\n'.join([code + ' : ' + self.mods[code].title +
		                      ' : ' + str(self.marks[code])
		                      for code in sorted(self.mods.keys())])
		pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
		if self.passed():
			outcome = 'Pass'
		elif self.passed_by_compensation():
			outcome = 'Pass by compensation'
		else:
			outcome = 'Fail'

		return '\n'.join([name, uline, results, pm, outcome])

	def add_mark(self, code, n):
		self.marks[code] = n

	def precision_mark(self):
		t = 0
		for key in self.marks.keys():
			mark = self.mods[key].ects * self.marks[key]
			t += mark

		return t / 60

	def passed(self):
		return all(n >= 40 for n in self.marks.values())

	def passed_by_compensation(self):
		cf = sum([self.mods[key].ects for key in self.marks.keys() if self.marks[key] >= 40])
		p = self.precision_mark() >= 45 and all(n >= 35 for n in self.marks.values()) and cf >= 50
		return p