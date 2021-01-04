'''                     instantiating a class
The process of creating a an object from a class.







'''
class Instructors:
    companyName = "Bluelime"  # I've defined the class on this line.

    def __init__(self,course):  # __init__ is a built-in function. It is called the initializer
        self.course = course  # I've created the variable.
    
    def printinfo(self):
        print("My company name is ", Instructors.companyName)

elearing = Instructors()