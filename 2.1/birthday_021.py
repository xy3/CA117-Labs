import sys
import calendar

dic = {
	0 : "Monday's child is fair of face",
	1 : "Tuesday's child is full of grace",
	2 : "Wednesday's child is full of woe",
	3 : "Thursday's child has far to go",
	4 : "Friday's child is loving and giving",
	5 : "Saturday's child works hard for a living",
	6 : "Sunday's child is fair and wise and good in every way",
}

def dayfinder(dob):
	d, m, y = int(dob[0]), int(dob[1]), int(dob[2])
	day = calendar.weekday(y, m, d)
	dayname = (dic[day]).split("'")[0]
	return "You were born on a {} and {}.".format(dayname, dic[day])

def main():
	print(dayfinder(sys.argv[1:]))

if __name__ == '__main__':
	main()