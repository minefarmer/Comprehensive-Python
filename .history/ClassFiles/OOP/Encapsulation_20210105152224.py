'''                 Encapsulation : Part 1
Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct data modification so it prevents accidental data modification.
Encapsulation basically allows the internal representation of an object to be hidden from the view outside of the objects definition.
Public methods and variables can be accessed from anywhere within the program.
Private methods and variables are accessible from their own class.
Double underscore prefix before object name makes it private'

           Encapsulation Part 2:     40











'''
# class Cars:
#     def __init__(self,speed, color):
#         self.speed = speed
#         self.color = color

#     def set_speed(self,value):
#         self.speed = value
    
#     def get_speed(self):
#         return self.speed









#           Encapsulation Part 2:     40
class Cars:
    def __init__(self,speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self,value):
        self.speed = value
    
    def get_speed(self):
        return self.speed

ford = Cars(250,"green")
nissan = Cars(300,"red")
toyota = Cars(350, "blue")

ford.set_speed()  # If I wanted to chang he value of the speed after the instantiantion, I can do that by using the name of the instance and the method.
