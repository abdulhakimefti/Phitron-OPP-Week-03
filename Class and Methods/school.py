class Student:
    def __init__(self,name,age,id):
        self.name =name
        self.age= name
        self.id = id

class Course :
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher

class Teacher :
    def __init__(self,name,course):
        self.name= name
        self.course = course

class School:
    def __init__(self,name,teacher,courses,student):
        self.name = name
        self.teacher = teacher
        self.courses = courses
        self.student = student

school_name ='Phitron'
ds_course = Course('Data Structure','Einstain')
teacher_1= Teacher('Einstain',ds_course)
algo_course = Course ('Algorithm','edison')
teacher_2 = Teacher('Edison',algo_course)

student_1= Student('Efti',18,2021392)
student_2 = Student('Abdul Hakim',19,23489)
student_3 = Student('Alia batt',29,45823)

teachers = [teacher_1,teacher_2]
courses=[ds_course,algo_course]
students= [student_1,student_2,student_3]

my_school = School(school_name,teachers,courses,students)
print(my_school.student)
print(type(student_1))
print(type(my_school))