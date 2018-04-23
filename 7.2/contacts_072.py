class Contact(object):
	def __init__(self, name, phone, email):
		self.n = name
		self.p = phone
		self.e = email

	def __str__(self):
		return "{} {} {}".format(self.n, self.p, self.e)

class ContactList(object):
	def __init__(self, d=None):
		if d == None: self.d = {}
		else: self.d = d

	def add_contact(self, contact):
		self.d[contact.n] = contact

	def get_contact(self, name):
		if name in self.d:
			return self.d[name]
		else:
			return "{} : No such contact".format(name)
	
	def del_contact(self, key):
		if key in self.d:
			del self.d[key]

	def __str__(self):
		a = []
		for key in self.d.keys():
			a.append(str(self.d[key]))

		return "Contact list\n------------\n" +"\n".join(sorted(a))