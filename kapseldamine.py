"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""
    def __init__(self, name = str, id = float, status = str):
        self.__name = name
        self.__id = id
        self.__status = "Active"
    
    def Student(self):
        Student.__name = name
        Student.__id = id
        Student.status = "Active"
    
    def get_id(self):
        return Student.id
    def set_name(self, name):
        Student.name = name
    
    def get_name(self):
        return Student.name
    
    def set_status(self, status):
        if Student.status == 'Active' or 'Expelled' or 'Finished' or 'Inactive':
            Student.status = "Active"
        else:
            pass
    
    def get_status(self):
        Student.get_status
    
    pass

