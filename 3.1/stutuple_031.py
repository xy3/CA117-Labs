def Student(firstname, surname, id):
	return firstname, surname, id

def show_student(s):
	t = ['First name: ', 'Surname: ', 'ID: ']
	print('{:>12}{}\n{:>12}{}\n{:>12}{}'.format(t[0],s[0],t[1],s[1],t[2],s[2]))
