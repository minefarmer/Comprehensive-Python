'''                 Creating a class
Created with the keyword class followed by a name,
Common practice is to make the names Pascal Casing:  Example: MyFirstCar
A class consists of variables(Attributes) and functions (Methods)
Classes can be used to model a lot of things.




'''
class Instructors:
    companyName = "Bluelime"  # I've defined the class on this line.

    def __init__(self,course):  # __init__ is a built-in function. It is called the initializer
        self.course = course  # I've created the variable.
    
    def printinfo(self):
        print("My company name is ", Instructors.companyName)

class Petsdatetime A combination of a date and a time. Attributes: ()