class Student:
    #Class Variable
    school_name="Golden School"
    def __init__(self, id, name, age, course):
        self.id=id
        self.name=name 
        self.age=age
        self.course=course
    #Instead of using display method for every instance,
    #We use class studentManger to add students and view students at once
    def display(self):
        return '{}: {} enrolled in {}'.format(self.id, self.name, self.course)
    def display_school(self):
        return '{} is student of {}'.format(self.name, self.school_name)
    def toFile_format(self):
        return f'{self.id}, {self.name}, {self.age}, {self.course}\n'