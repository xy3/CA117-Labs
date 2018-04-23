from stack_092 import Stack

class Queue(object):
	def __init__(self):
		self.l = []
	def enqueue(self, n):
		self.l.append(n)
	def dequeue(self):
		return self.l.pop(0)
	def __len__(self):
		return len(self.l)

def ifl(n):
	try: float(n)
	except ValueError: return False
	return True

def calculator(s):
	stack, q = Stack(), Queue()
	s = s.split()

	i = 0
	while i < len(s) and ifl(s[i]):
		stack.push(float(s[i]))
		i += 1

	for c in s[i:]: q.enqueue(c)

	while len(q) > 0:
		calc, n1 = q.dequeue(), stack.pop()

		if calc == 'r': stack.push(n1 ** (1/2))
		elif calc.isalpha(): stack.push(n1 * -1)
		else: stack.push(eval(str(stack.pop()) + calc + str(n1)))
	

	return stack.pop()