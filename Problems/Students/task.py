class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year


n = input()
ln = input()
by = input()

student_id = Student(n, ln, by)
print(student_id.id)
