class StudentManager:
    def __init__(self):
        #creating an empty list to store students
        self.students=[]
    
    def add_students(self, student): #self -> manager instance , student-> Student instances(stud1, stud2 )
        self.students.append(student)
    
    def view_students(self):
        for student in self.students:
            print(student.display())
            #print(student.display_school())
    
    def delete_students(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
    
    def  update_students(self,id, name, age, course):
        for student in self.students:
            if student.id == id:
                student.name=name
                student.age=age
                student.course=course
    
    def search_student(self, id):
        for student in  self.students:
            if student.id == id:
                return student.display()
        return '{} not found'.format(id)
    
    
                
