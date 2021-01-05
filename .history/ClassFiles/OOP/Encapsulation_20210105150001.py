'''                 Encapsulation : Part 1
Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct data modification so it prevents accidental data modification.
Encapsulation basically allows the internal representation of an object to be hidden from the view outside of the objects definition.
Public methods and variables can be accessed from anywhere within the program.
Private methods and variables are accessible from their own class.
Double underscore prefix before object name makes it private'













'''
class Cars:
    def __init__(self,speed, color):
