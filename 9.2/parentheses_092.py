from stack_092 import Stack

def matcher(line):
	l, r = ("[{("), (")}]")
	rb = Stack()
	cb = Stack()
	sb = Stack()