class Validator:
    def is_duplicate(self, manager, new_id):
        for student in manager.students:
            if student.id == new_id:
                 return True
        return False
    
    #Validating Name
    def is_valid_name(self,name):
        return bool(name.strip())
    
    #Checking if the age is valid or not
    def is_valid_age(self, age):
        return 0 < age < 30