from models.student import Student
from services.student_manager import StudentManager
from validators.validator import Validator

manager=StudentManager()
manager.load_students()
validator=Validator()

while True:
    print("1.View students")
    print("2.Add Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")

    choice=int(input("Enter your choice: "))
    match choice:
       # View Students #
       case 1:
        manager.view_students()

       # Add Student #
       case 2:
        id=int(input("Enter id: "))
        #Check id exist or not by validators
        if validator.is_duplicate(manager, id):
            print("Student with id {} already exists".format(id))
            continue
        else:
           name=input("Enter name of the student:")
           if not validator.is_valid_name(name):
               print("Invalid name. Please try again.")
               continue
           try:
              age=int(input("Enter the age:"))
           except ValueError:
              print("Invalid age. Please enter a number.")
              continue
           if not validator.is_valid_age(age):
              continue
           course=input("Enter the enroled course:")
           new_student=Student(id, name, age, course)
           manager.add_students(new_student)
           print("Student added successfully")
           
           manager.view_students()

        # Search Student #
       case 3:
          id=int(input("Enter id to search: "))
          print(manager.search_student(id))
       
       # Update Student #
       case 4:
          id=int(input("Enter id to update:"))
          name=input("Enter name of the student:")
          if not validator.is_valid_name(name):
             print("Invalid name. Please try again.")
             continue
          try:
             age=int(input("Enter the age:"))
          except ValueError:
             print("Invalid age. Please enter a number.")
             continue
          if not validator.is_valid_age(age):
             print("Age should be less than 30")
             continue         
          course=input("Enter the enroled course:")    
          manager.update_students(id, name, age, course)
          print("Student updated successfully") 
          manager.view_students()
        
        # Delete Student #
       case 5:
          id=int(input("Enter the id to delete:"))
          manager.delete_students(id)
          print("Student deleted successfully")
          manager.view_students()
       case _:
            print("Invalid choice. Please try again.")
    

    





