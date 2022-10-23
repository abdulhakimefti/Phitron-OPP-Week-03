
class Student:
    id = 1
    def __init__(self,name,mark):
        self.student_name = name
        self.mark= mark
        self.student_id=Student.id
        Student.id+=1

studentList = []
totalStudent=input('Total Student : ')
for i in range(int(totalStudent)):
    name= input('Stueden Name : ')
    mark= input('Student marks : ')
    studentList.append(Student(name,int(mark)))
with open('student.txt','w') as fileWrite:
    for i in studentList:
        fileWrite.write(f'id: {i.student_id}\n')
        fileWrite.write(f'Name: {i.student_name}\n')
        fileWrite.write(f'Marks: {i.mark}\n')

