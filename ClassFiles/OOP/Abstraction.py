'''                 Abstraction : Part 1
Abstraction hides the internal details and shows only functionalities that are.

    Abstract Classes:
They are classes that contain one or more abstract methods.
They cannot be instantiated. That means I cannot create an instance object from an abstract class.
They require subclasses to provide implementation for the abstract methods.
Subclasses of an abstract class in Python are not required to Implement abstract methods of the parent class.

    Abstract Methods:
They are methods that are declared but contains no implementation.
Requires subclass to provide implementation for them.

Abstraction  Part 2  #50
Python does not on it's own provide abstract classes.
However, Python comes with a module which provides th infrastructure that allows you to define abstract classes. And the name of the module is called A B C => Abstract Base Classes
Whatever method I have in the parent class. I have to implement it in the subclass because of the abstraction.












'''
# class Shape:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def__init__(self,side):
#         self.side = side

# myShape = Shape()








# Abstraction  Part 2
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod # A decorator allows me to add new functionality to an existing object (classes, methods, functions) without modifying its structure.
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

# myShape = Shape()  # Traceback (most recent call last):
#                 # File "/home/rich/CarlsHub/Comprehensive-Python/ClassFiles/OOP/Abstraction.py", line 54, in <module>
#                 #     MyShape = Shape()
#                 # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter



# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod # A decorator allows me to add new functionality to an existing object (classes, methods, functions) without modifying its structure.
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

# # myShape = Shape()

# mysquare = Square()  # Traceback (most recent call last):
#                 # File "/home/rich/CarlsHub/Comprehensive-Python/ClassFiles/OOP/Abstraction.py", line 86, in <module>
#                 #     mysquare = Square()
#                 # TypeError: Can't instantiate abstract class Square with abstract methods area, perimeter
# ______%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod # A decorator allows me to add new functionality to an existing object (classes, methods, functions) without modifying its structure.
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side

    def area(self):
        return self.__side* self.__side
    
    def perimeter(self):
        return 4 * self.__side

# myShape = Shape()

mysquare = Square(5)

print(mysquare.area())  # 25
print(mysquare.perimeter())  # 20

