class BankAccount(object):

	next_account_number = 16555232
	total_lodgements = 0
	interest_rate = 0.043

	def __init__(self, forename, surname, balance=0, account_number=None):
		self.fnm = forename + " " + surname
		
		if account_number == None: 
			self.acc = BankAccount.next_account_number
		else: self.acc = account_number
		
		self.bal = balance
		BankAccount.next_account_number += 1
	
	def __str__(self):
		l = []
		l.append("Name: {}".format(self.fnm))
		l.append("Account number: {}".format(self.acc))
		l.append("Balance: {:.2f}".format(self.bal))
		return "\n".join(l)

	def __iadd__(self, n):
		self.bal += n
		return self

	def apply_interest(self):
		self.bal *= (1 + self.interest_rate)
		BankAccount.total_lodgements += 1

	def lodge(self, n):
		self.bal += n
		BankAccount.total_lodgements += 1
