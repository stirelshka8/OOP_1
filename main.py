class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def print_grades(self):
        print(self.grades)

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    # TODO: Добавить перегрузку магического метода __str__
       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
     
 
class Lecturer(Mentor): # Добавил подкласс Lecture
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} #  Атрибут-список для выставления оценок Lecture(в котором ключи – названия курсов, а значения – списки оценок)

    # TODO: Добавить перегрузку магического метода __str__

class Reviewer(Mentor): # Добавил подкласс Reviewer
    def __init__(self, name, surname):
        super().__init__(name, surname)
   
    def rate_hw(self, student, course, grade): # Данный метод перемещен из класса Mentor в подкласс Reviewer
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # TODO: Добавить перегрузку магического метода __str__


cool_reviewer = Reviewer('Some', 'Buddy')
best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_lecture = Lecturer('Bob', 'Bobson')

cool_reviewer.courses_attached += ['Python']
cool_lecture.courses_attached += ['Python']

best_student.courses_in_progress += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lectur(cool_lecture, 'Python', 10)
best_student.rate_lectur(cool_lecture, 'Python', 9)
best_student.rate_lectur(cool_lecture, 'Python', 8)


print(best_student.print_grades())
print(cool_lecture.print_grades())
