'''                     instantiating a class
The process of creating a an object from a class.
If I want to access an instance of a class, I could do that by typing in:  ObjectName.method = ('name of the method)
        i.e. line 24
I can access an attribute that belongs to a class from an instance of the class, I can by using object name, followed by a dot notation and then the name of the attribute.  ObjectName.Attribute




'''
class Instructors:
    companyName = "Bluelime"  # I've defined the class on this line.

    def __init__(self,course):  # __init__ is a built-in function. It is called the initializer
        self.course = course  # I've created the variable.
    
    def printinfo(self):
        print("My company name is ", Instructors.companyName)

elearning = Instructors("Python for Beginners")  # instantiated a class

bls = Instructors("Django for Beginners")  # a variable  second instance of the class.

bls.printinfo()  # My company name is  Bluelime

print(bls.course)