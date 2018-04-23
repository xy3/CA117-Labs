class Element(object):
	def __init__(self, num, name, sym, bp):
		self.num, self.name, self.sym, self.bp = str(num), name, sym, str(bp)

	def print_details(self):
		print("Number: " +self.num)
		print("Name: " +self.name)
		print("Symbol: " +self.sym)
		print("Boiling point: " +self.bp + " K")
