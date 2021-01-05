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

# ford.set_speed(450)  # If I wanted to chang he value of the speed after the instantiantion, I can do that by using the name of the instance and the method.

ford.speed = 500  #  I can also access the speed variable directly without the method and change the value. I'm able to do this because there is no encapsulation in place.

print(ford.get_speed())  # 500
print(ford)  # <__main__.Cars object at 0x000002AA04FC60A0>
print(ford.color)  
