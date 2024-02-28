"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""
    
    def __init__(self, name = str, id = float, status = "Active"):
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def Student(self):
        Student.__name = name
        Student.__id = id
        Student.__status = "Active"
        
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_status(self, status):
        if self.__status == "Active" or "Expelled" or "Finished" or "Inactive":
            self.__status = "Active"
        else:
            pass
    
    def get_status(self):
        return self.__status
    
    
    pass
