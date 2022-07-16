class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                if grade <= 10:
                    lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не в классе Student")
            return
        return self.name < other.name


    def _val_grades(self):
        for self.values in self.grades.values():
            self.temp_keys = 0
            for self.val in self.values:
               self.temp_keys += self.val
            return self.temp_keys // len(self.values) # Так как в заднии сказанно среднее значение, вот я и использовал
                                                      # челочисленное деление
                
# Код ниже выглядит просто ужасно. Но, вывод красив)
    def __str__(self):
        return str(f'Студент\nИмя: {self.name} \n\
Фамилия: {self.surname}\n\
Средняя оценка за домашнее задание: {self._val_grades()}\n\
Курсы в процессе изучени: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}\n\n')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
     
 
class Lecturer(Mentor): # Добавил подкласс Lecture
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} #  Атрибут-список для выставления оценок Lecture(в котором ключи – названия курсов, а значения – списки оценок)

    def _val_grades(self):
        for self.values in self.grades.values():
            self.temp_keys = 0
            for self.val in self.values:
               self.temp_keys += self.val
            return self.temp_keys // len(self.values)# Так как в заднии сказанно среднее значение, вот я и использовал
                                                     # челочисленное деление
                

    def __str__(self):
        return str(f'Лектор\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._val_grades()}\n\n')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не в классе Lecturer")
            return
        return self.name < other.name


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
    
    def __str__(self):
        return str(f'Проверяющий\nИмя: {self.name} \nФамилия: {self.surname}\n\n')




cool_reviewer = Reviewer('Some', 'Buddy')
best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_lecture = Lecturer('Bob', 'Bobson')

cool_reviewer.courses_attached += ['Python']
cool_lecture.courses_attached += ['Python']
best_student.finished_courses += ['C++, C#']

best_student.courses_in_progress += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 9)

best_student.rate_lectur(cool_lecture, 'Python', 8)
best_student.rate_lectur(cool_lecture, 'Python', 10)
best_student.rate_lectur(cool_lecture, 'Python', 5)

print(cool_reviewer)
print(cool_lecture)
print(best_student)

