from datetime import datetime


class Human:
    def __init__(self, id, name, birth_year):
        self.id = id
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        now = datetime.now()
        return now.year - self.birth_year

    def __str__(self) -> str:
        return f"""ID\t: {self.id}
Name\t: {self.name}
Age\t: {self.age}"""


class Student(Human):
    def __init__(self, id, name, birth_year, marks=None):
        super().__init__(id, name, birth_year)
        if marks is None:
            self.marks = []
        else:
            self.marks = marks

    def __str__(self) -> str:
        return super().__str__() + f'\nMarks\t: {" ".join(map(str, self.marks))}'


class Teacher(Human):
    def __init__(self, id, name, birth_year, salary=None):
        super().__init__(id, name, birth_year)
        self.salary = salary

    def set_salary(self, salary):
        if self.salary < 0:
            raise ValueError("Invalid salary")

        self.salary = salary


student_one = Student("SV001", "John", 1992)
teacher_one = Teacher("T001", "Jack", 1996)

student_one.marks = [9.8, 7.8, 5.6]

print(student_one)
print(teacher_one)
