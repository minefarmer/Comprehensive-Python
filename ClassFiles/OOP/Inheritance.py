'''                 Inheritance : Part 1
Inheritance is one o the key concepts of object oriented programming.
Inheritance is basically the process that allows us to create a new class and reusing the code from a existing parent class.
This code ill contain both methods and attributes of the parent class.
The parent class (superclass or base class) is the class being inherited from.
The child class (subclass or derived ) is the class tht inherits from another class.


                    Inheritance : Part 2  # 40
Creating a child class that will inherit from the parent class,


                    Inheritance : Part 3  # 50
Adding a __init__() to my child class  # It will over ride the __init__ of the parent class,


                    Inheritance : Part 4  # 110

                    Inheritance : Part 1
'''     ##  a very basic class
# class Person:
#     def __init__(self,fname,lname):
#         self.first_name = fname  # a variable
#         self.last_name = lname  # a variable

#     def printname(self):
#         print(self.first_name, self.last_name)

# florist = Person("Jane","Flowers")  # I've instantiated this class called pesron.
# florist.printname()  # Jane Flowers









#                     # Inheritance : Part 2

# class Lawyers(Person):
#     pass  # By using pass 'Lawyers' now has the same attributes and methods as the parent class bh inheriting the parent class called Person.
# happy_lawyers = Lawyers("Jack","Smiley")  # I'm creating a variable.
# happy_lawyers.printname()  # Jack Smiley




# Inheritance : Part 3   ## pass is removed
# class Person:
#     def __init__(self,fname,lname):
#         self.first_name = fname  # a variable
#         self.last_name = lname  # a variable

#     def printname(self):
#         print(self.first_name, self.last_name)

# florist = Person("Jane","Flowers")  # I've instantiated this class called pesron.
# florist.printname()  # Jane Flowers

# class Lawyers(Person):
#     def __init__(self,fname,lname):  # This __init__ overrides the parent class,
#         self.first_name = fname  # a variable
#         self.last_name = lname  # a variable

#     def printinfo(self):
#         print(self.first_name, self.last_name)



# happy_lawyers = Lawyers("Rich","Matson")
# happy_lawyers.printname()  # Rich Matson
# happy_lawyers.printinfo()  # Rich Matson




# class Person:
#     def __init__(self,fname,lname):
#         self.first_name = fname  # a variable
#         self.last_name = lname  # a variable

#     def printname(self):
#         print(self.first_name, self.last_name)

# florist = Person("Jane","Flowers")  # I've instantiated this class called pesron.
# florist.printname()  # Jane Flowers

# class Lawyers(Person):
#     def __init__(self,fname,lname):  # This __init__ overrides the parent class,
#         Person.__init__(self,fname,lname)
#         # self.first_name = fname  # a variable
#         # self.last_name = lname  # a variable

#     def printinfo(self):
#         print(self.first_name, self.last_name)



# happy_lawyers = Lawyers("Rich","Matson")
# happy_lawyers.printname()  # Rich Matson







                                # Inheritance : Part 4 
class Person:
    def __init__(self,fname,lname):
        self.first_name = fname  # a variable
        self.last_name = lname  # a variable

    def printname(self):
        print(self.first_name, self.last_name)

florist = Person("Jane","Flowers")  # I've instantiated this class called pesron.
florist.printname()  # Jane Flowers

class Lawyers(Person):
    def __init__(self,fname,lname,casetype):  # This __init__ overrides the parent class,
        Person.__init__(self,fname,lname)
        self.casetype = casetype

        # self.first_name = fname  # a variable
        # self.last_name = lname  # a variable

    def printinfo(self):
        print("Hello my name is ",self.first_name, self.last_name)  # Hello my name is  Rich Matson



happy_lawyers = Lawyers("Rich","Matson","criminal")
happy_lawyers.printname()  # Rich Matson
happy_lawyers.printinfo()  # Rich Matson

print(happy_lawyers.casetype)  # casetype
