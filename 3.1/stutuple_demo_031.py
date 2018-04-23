import stutuple_031 as stutuple

student1 = stutuple.Student('Joe', 'Mannion', 98365338)
student2 = stutuple.Student('Louise', 'Callaghan', 99324761)
student3 = stutuple.Student(firstname='Noel', id=99071239, surname='Rooney')
stulist = [student1, student2, student3]

for s in stulist:
    stutuple.show_student(s)