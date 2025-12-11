class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade
    def set_average_grade (self, new_grade):
        self.average_grade =new_grade
    def info(self):
        print(f"Студент: {self.name} {self.surname}, вік: {self.age}, середній бал: {self.average_grade}")
Student1=Student(name="Олексій", surname="Євплов", age=39, average_grade=90)
Student1.info()
Student1.set_average_grade(100)
Student1.info()    