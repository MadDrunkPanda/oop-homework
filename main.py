class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_progress = []
        self.grades = {}

    # Оцениваем лекторов
    def lect_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_progress and course in lecturer.courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print(f'{lecturer.surname} {lecturer.name} не читает лекции по курсу {course}')

    # Переназначаем выдачу у студентов
    def __str__(self):
        list1 = []
        for gr in self.grades.values():
            list1 += gr
        x = f'{sum(list1) / len(list1):.1f}'
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредний балл за все ДЗ: {x}\nКурсы в процессе:  {','.join(self.courses_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"
        return res

    # Параметры сравнения
    def __lt__(self, other, course):
        if isinstance(other, Student) and course in self.grades and course in other.grades:
            if sum(self.grades[course]) / len(self.grades[course]) < sum(other.grades[course]) / len(
                    other.grades[course]):
                return True
            else:
                return False
        else:
            result = f"Сравнение невозможно"
            return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades = {}

    # Переназначаем выдачу у лектора
    def __str__(self):
        list1 = []
        for gr in self.grades.values():
            list1 += gr
        y = f'{sum(list1) / len(list1):.1f}'
        x = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {y}"
        return x

    # Параметры сравнения для лекторов
    def __lt__(self, other, course):
        if isinstance(other, Lecturer) and course in self.grades and course in other.grades:
            if sum(self.grades[course]) / len(self.grades[course]) < sum(other.grades[course]) / len(
                    other.grades[course]):
                return True
            else:
                return False


class Reviewer(Mentor):
    stud_grades = {}

    # Оценка студентам + сохраняем их в атрибут, чтобы потом получить средний балл по курсу
    def stud_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses_progress:
            if course in student.grades and course in self.stud_grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print(f'{student.surname} {student.name} не проходит обучение по курсу {course}')
        if course in self.stud_grades:
            self.stud_grades[course] += [grade]
        else:
            self.stud_grades[course] = [grade]

    # Переназначаем выдачу для ревьюера
    def __str__(self):
        x = f"Имя: {self.name}\nФамилия: {self.surname}"
        return x

    # Получаем средний балл по курсу у студентов(без создания списка студентов вручную)
    def students_arythm(self, course):
        list1 = []
        for gr in self.stud_grades.values():
            list1 += gr
        mid = f'Средний балл по курсу {course} у всех студентов: {sum(list1) / len(list1):.1f}'
        return mid


stud1 = Student('Иван', 'Петров', 'мужской')
stud2 = Student('Мария', 'Сидорова', 'женский')
rev1 = Reviewer('Анна', 'Иванова')
rev2 = Reviewer('Зевс', 'Юпитеров')
lect1 = Lecturer('Антон', 'Антонов')
lect2 = Lecturer('Гомер', 'Симпсон')

stud1.finished_courses.append('Введение в программирование')
stud1.courses_progress.append('Git')
stud1.courses_progress.append('Python')

stud2.finished_courses.append('Введение в программирование')
stud2.courses_progress.append('Git')
stud2.courses_progress.append('Python')

rev1.courses.append('Введение в программирование')
rev1.courses.append('Git')
rev1.stud_grade(stud1, 'Git', 10)
rev1.stud_grade(stud1, 'Git', 8)
rev1.stud_grade(stud1, 'Git', 10)
rev1.stud_grade(stud2, 'Git', 10)
rev1.stud_grade(stud2, 'Git', 9)
rev1.stud_grade(stud2, 'Git', 10)

rev2.courses.append('Введение в программирование')
rev2.courses.append('Python')
rev2.stud_grade(stud1, 'Python', 7)
rev2.stud_grade(stud1, 'Python', 8)
rev2.stud_grade(stud1, 'Python', 6)
rev2.stud_grade(stud2, 'Python', 8)
rev2.stud_grade(stud2, 'Python', 9)
rev2.stud_grade(stud2, 'Python', 9)

lect1.courses.append('Python')
lect1.courses.append('Git')

lect2.courses.append('Python')
lect2.courses.append('Git')

stud1.lect_grade(lect1, 'Git', 10)
stud1.lect_grade(lect1, 'Git', 10)
stud1.lect_grade(lect1, 'Git', 9)
stud1.lect_grade(lect2, 'Git', 3)
stud1.lect_grade(lect2, 'Git', 2)
stud1.lect_grade(lect2, 'Git', 3)
stud1.lect_grade(lect1, 'Python', 10)
stud1.lect_grade(lect1, 'Python', 10)
stud1.lect_grade(lect1, 'Python', 10)
stud1.lect_grade(lect2, 'Python', 2)
stud1.lect_grade(lect2, 'Python', 2)
stud1.lect_grade(lect2, 'Python', 3)

stud2.lect_grade(lect1, 'Git', 10)
stud2.lect_grade(lect1, 'Git', 10)
stud2.lect_grade(lect1, 'Git', 10)
stud2.lect_grade(lect2, 'Git', 2)
stud2.lect_grade(lect2, 'Git', 2)
stud2.lect_grade(lect2, 'Git', 1)
stud2.lect_grade(lect1, 'Python', 10)
stud2.lect_grade(lect1, 'Python', 9)
stud2.lect_grade(lect1, 'Python', 10)
stud2.lect_grade(lect2, 'Python', 1)
stud2.lect_grade(lect2, 'Python', 2)
stud2.lect_grade(lect2, 'Python', 3)

# Создаем список лекторов для вывода средней оценки по курсам
lect_list = []
lect_list.append(lect1.grades)
lect_list.append(lect2.grades)


# Функция считает средний лекторский балл по конкретному курсу
def mid_lect(list_in, course):
    l_list = []
    for dict in list_in:
        for key, gr in dict.items():
            if key == course:
                l_list += gr
    mid = f'Средняя оценка лекторов по курсу {course}: {sum(l_list) / len(l_list):.1f}'
    return mid

print(mid_lect(lect_list, 'Python'))
print(rev1.students_arythm('Git'))