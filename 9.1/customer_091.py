class Customer(object):

	def __init__(self, nme, bal, ad1, ad2, ad3):
		self.discount = 0
		self.n = nme
		self.b = bal
		self.a1 = ad1
		self.a2 = ad2
		self.a3 = ad3


	def owes(self):
		return float(self.b * (1 - (self.discount/100)))

	def __str__(self):
		l = []
		l.append(self.n)
		l.append(self.a1)
		l.append(self.a2)
		l.append(self.a3)
		l.append("Balance: {:.2f}".format(self.b))
		l.append("Discount: {}%".format(self.discount))
		l.append("Amount due: {:.2f}".format(self.owes()))
		return "\n".join(l)


class ValuedCustomer(Customer):

	def __init__(self, nme, bal, ad1, ad2, ad3):
		super().__init__(nme, bal, ad1, ad2, ad3)
		self.discount = 10

	def __str__(self):
		return super().__str__()
