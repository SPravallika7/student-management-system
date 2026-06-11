
from models.student import Student


class StudentManager:
    def __init__(self):
        #creating an empty list to store students
        self.students=[]
    
    #Saving syudents after updation or delete
    def save_students(self):
        with open('data/students.txt', 'w') as file:
            for student in self.students:
                file.write(student.toFile_format())
    #Loading students from file to list to restore data when we run the program again
    def load_students(self): 
        with open('data/students.txt', 'r') as file:
            for line in file:
               
                id, name, age, course = line.strip().split(',')

                student = Student(
                int(id),
                name,
                int(age),
                course
             )

                self.students.append(student)

        
    
    def add_students(self, student): #self -> manager instance , student-> Student instances(stud1, stud2 )
        print(self.students.append(student))
        with open('data/students.txt', 'a') as file:
              file.write(student.toFile_format())
    
    def view_students(self):
        for student in self.students:
            print(student.display())
            #print(student.display_school())
    
    def delete_students(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                self.save_students()
    
    def  update_students(self,id, name, age, course):
        for student in self.students:
            if student.id == id:
                student.name=name
                student.age=age
                student.course=course
                self.save_students()
    
    def search_student(self, id):
        for student in  self.students:
            if student.id == id:
                return student.display()
        return '{} not found'.format(id)
    
    
                
