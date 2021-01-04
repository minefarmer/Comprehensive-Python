'''                         Modifying Classes
Add new attributes  # 9
Modify existing attribute values.  # 25
Delete attributes.  # 61
                                    Importing Classes
They can be imported into other programs like python modules.


# To see the original == go to  InstantiatingAClass.py
# '''
# class Instructors:
#     companyName = "Bluelime"  # I've defined the class on this line.

#     def __init__(self,course,duration):  # duration is an added attribute.
#         self.course = course  # I've created the variable.
#         self.duration = duration  # This is now a default value that has been added
    
#     def printinfo(self):
#         print("My company name is ", Instructors.companyName)

# elearning = Instructors("Python for Beginners",7)  # 7 is the duration i've just added.

# bls = Instructors("Django for Beginners",8)  # 8 is the duration i've just added.

# bls.course = "HTML"  # Changes the name of the course on line 23.

# bls.printinfo()  # My company name is  Bluelime

# print(bls.course)  # HTML

# print(bls.duration)  # 8  ## This is how I cn access the new attribute on line 13.







class Instructors:
    companyName = "Bluelime"  # I've defined the class on this line.

    def __init__(self,course,duration):  # duration is an added attribute.
        self.course = course  # I've created the variable.
        self.duration = duration  # This is now a default value that has been added
    
    def printinfo(self):
        print("My company name is ", Instructors.companyName)

elearning = Instructors("Python for Beginners",7)  # 7 is the duration i've just added.

bls = Instructors("Django for Beginners",8)  # 8 is the duration i've just added.

bls.course = "HTML"  # Changes the name of the course on line 23.

bls.printinfo()  # My company name is  Bluelime

print(bls.course)  # HTML

del bls.duration

print(bls.duration)  # Traceback (most recent call last):
                    # File "/home/rich/CarlsHub/Comprehensive-Python/ClassFiles/OOP/ModifyingClass.py", line 61, in <module>
                    #     print(bls.duration)  # 8  ## This is how I cn access the new attribute on line 13.
                    # AttributeError: 'Instructors' object has no attribute 'duration'