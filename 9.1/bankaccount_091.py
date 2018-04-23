class BankAccount:
	account_type = 'General'
	next_account_number = 16555232

	def __init__(self, forename, surname, balance):
		self.forename = forename
		self.surname = surname
		self.balance = balance
		self.account_number = self.next_account_number
		BankAccount.next_account_number += 1


	def lodge(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds available")

	def __str__(self):
		s = 'Name: {} {}'.format(self.forename, self.surname)
		s += '\nAccount number: {}'.format(self.account_number)
		s += '\nAccount type: {}'.format(self.account_type)
		s += '\nBalance: {:.2f}'.format(self.balance)
		return s


class CurrentAccount(BankAccount):
	account_type = 'Current'
	overdraft = 1000.00

	def withdraw(self, amount):
		if self.balance + self.overdraft >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds available")

	def __str__(self):
		s = 'Name: {} {}'.format(self.forename, self.surname)
		s += '\nAccount number: {}'.format(self.account_number)
		s += '\nAccount type: {}'.format(self.account_type)
		s += '\nBalance: {:.2f}'.format(self.balance)
		s += '\nOverdraft: -{:.2f}'.format(self.overdraft)
		return s


class SavingsAccount(BankAccount):
	account_type = 'Savings'
	interest_rate = 0.01

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds available")

	def apply_interest(self):
		self.balance *= 1 + self.interest_rate

	def __str__(self):
		s = 'Name: {} {}'.format(self.forename, self.surname)
		s += '\nAccount number: {}'.format(self.account_number)
		s += '\nAccount type: {}'.format(self.account_type)
		s += '\nBalance: {:.2f}'.format(self.balance)
		s += '\nInterest rate: {:.2f}'.format(self.interest_rate)
		return s