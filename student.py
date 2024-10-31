class Student:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class Teacher:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class Sinif:
    def __init__(self,sinif):
        self.sinif = sinif

class Department:
    def __init__(self,department):
        self.department = department

class Lesson:
    def __init__(self, lesson_name):
        self.lesson_name = lesson_name

name = input("Öğrenci Adını Giriniz.-->")
surname = input("Öğrenci Soyadını Giriniz.-->")

teacherName = input("Öğretmenin Adını Giriniz.-->")
teacherSurname = input("Öğretmenin Soyadını Giriniz.-->")

studentClass = input("Sınıfınızı giriniz-->")
studentDepartment = input("Şube giriniz-->")

student = Student(name,surname)
teacher = Teacher(name,surname)

sinif = Sinif(studentClass)
departmen = Department(studentDepartment)

lessons = []
while True:
    studentLesson=input("Almak İstediğiniz Dersi Giriniz -->")
    lesson = Lesson(studentLesson)
    lessons.append(studentLesson)

    option = input("Yeni bir ders almak istiyor musunuz ?: (E/H): ")

    if option.upper() == 'H':
        break
print("\n Öğrenci Adı: ",name,surname)
print("Eğitmen Adı: ",teacherName,teacherSurname)
print("Sınıf: ",studentClass)
print("Şube: ",studentDepartment)
print("Seçtiğiniz Dersler: ",lessons)